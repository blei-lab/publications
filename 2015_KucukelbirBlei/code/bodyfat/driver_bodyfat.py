#!/usr/local/bin/python

"""Driver

Usage:
  driver.py [--filename=FILENAME]

Options:
  --filename=FILENAME     Filename
  -h --help               Show this help message and exit

"""

import os, sys, datetime
from time import time
from docopt import docopt

import numpy as np
from scipy.special import gammaln
from scipy.stats import multivariate_normal

from bayes_linear_reg_analytic import *
from bayes_linear_reg_analytic_bt import *

import numpy.core.arrayprint as arrayprint
import contextlib

import sklearn.datasets

@contextlib.contextmanager
def printoptions(strip_zeros=True, **kwargs):
  origcall = arrayprint.FloatFormat.__call__
  def __call__(self, x, strip_zeros=strip_zeros):
      return origcall.__call__(self, x, strip_zeros)
  arrayprint.FloatFormat.__call__ = __call__
  original = np.get_printoptions()
  np.set_printoptions(**kwargs)
  yield
  np.set_printoptions(**original)
  arrayprint.FloatFormat.__call__ = origcall

def eformat(f, prec, exp_digits):
    s = "%.*e"%(prec, f)
    mantissa, exp = s.split('e')
    # add 1 to digits as 1 is taken by sign +/-
    return "%se%+0*d"%(mantissa, exp_digits+1, int(exp))

def log_pdf_studentT_multivar(x,mu,Sigma,df):
  '''
  logarithm of a multivariate student T pdf
  (numerically stable)
  '''
  D = mu.size
  x_minus_mu = x - mu[:,0]
  result = 0.0

  first_part  = gammaln(0.5*(df+D)) - gammaln(0.5*df) - 0.5*D*np.log(df*np.pi)
  (s, logdet) = np.linalg.slogdet(Sigma)

  quad_form   = 1/df * ( np.dot( x_minus_mu.T, np.linalg.solve(Sigma,x_minus_mu) ) )
  second_part = -0.5*(df+D) * np.log(1 + quad_form)
  result      = first_part -0.5*logdet + second_part

  return result

def log_pdf_studentT_univar(x,mu,Sigma,df):
  '''
  logarithm of a univariate student T pdf
  '''
  x_minus_mu = x - mu
  result = 0.0

  first_part  = gammaln(0.5*(df+1)) - gammaln(0.5*df) - 0.5*np.log(df*np.pi)
  logdet      = np.log(np.abs(Sigma))

  quad_form   = 1/df * ( x_minus_mu**2 / Sigma )
  second_part = -0.5*(df+1) * np.log(1 + quad_form)
  result      = first_part -0.5*logdet + second_part

  return result

def log_predictive_bayes_lin_reg(dat, blr):
  N = dat['design_matrix'].shape[0]
  result = 0.0
  for i in range(N):
    predictive_mean  = np.dot(dat['design_matrix'][i,:],blr['w_N'])
    predictive_scale = (blr['b_N'] / blr['a_N']) * \
                       (
                        1 + \
                        np.dot(
                          np.dot(dat['design_matrix'][i,:],blr['V_N']),
                          dat['design_matrix'][i,:].T)
                        )
    predictive_df    = 2*blr['a_N']
    result += log_pdf_studentT_univar(dat['y_noisy'][i],predictive_mean,predictive_scale,predictive_df)
  return np.squeeze(result)

def main():
  # Created formatted datetime string
  date_time_string = datetime.datetime.fromtimestamp(time()). \
                     strftime('%Y-%m-%d__%H_%M_%S')
  print "THIS IS driver_bodyfat.py -> TIMECODE: " + date_time_string

  # Create log file
  log_filename = date_time_string + "_LOG.txt"
  f = open(log_filename,'w')

  # Parse input
  args = docopt(__doc__)
  try:
    filename = args['--filename']
  except:
    exit("(--filename) is not valid.")

  ## DATASET

  X_train, y_train = sklearn.datasets.load_svmlight_file(filename)

  design_matrix    = X_train.toarray()
  y_noisy          = y_train

  my_G = 0.0;

  num_for_train = 200
  total_num     = 252

  split_indexTRAIN   = np.random.choice(total_num, num_for_train, replace=False)
  orig_index    = np.arange(total_num)
  split_indexTEST = np.setdiff1d(orig_index,split_indexTRAIN)


  training_data = {}
  training_data['design_matrix'] = design_matrix[split_indexTRAIN,:]
  training_data['y_noisy'] = y_noisy[split_indexTRAIN]

  testing_data = {}
  testing_data['design_matrix'] = design_matrix[split_indexTEST,:]
  testing_data['y_noisy'] = y_noisy[split_indexTEST]


  # Compute posterior
  blr = bayes_linear_reg_analytic(training_data, g=my_G)

  ## Calculate summary of posteriors
  # Posterior on weights is a multivariate t
  df = 2*blr['a_N']
  post_weights_mean = blr['w_N']
  post_weights_cov  = (df / (df-2.0)) * blr['V_N']

  # Posterior on variance is an inverse gamma
  post_variance_mean = blr['b_N'] / (blr['a_N'] - 1)
  post_variance_var  = (blr['b_N']**2) / ((blr['a_N'] - 1)**2 * (blr['a_N'] - 2))

  # Calculate predictive results on testing data
  # Predictive on new data is a multivariate t
  predictive_mean  = np.dot(testing_data['design_matrix'],blr['w_N'])
  predictive_scale = (blr['b_N'] / blr['a_N']) * \
                     (
                      np.identity(testing_data['design_matrix'].shape[0]) + \
                      np.dot(
                        np.dot(testing_data['design_matrix'],blr['V_N']),
                        testing_data['design_matrix'].T)
                      )
  predictive_df    = 2*blr['a_N']


  # Print the results
  print >>f, " "
  with printoptions(precision=3, suppress=True, strip_zeros=False):
    print >>f, "The posterior mean : ",
    print >>f, np.squeeze(blr['w_N'])
    print >>f, "The predictive df  : ",
    print >>f, np.squeeze(predictive_df)
    print >>f, " "

    print >>f, "BAYES"
    print >>f, "The average log predictive (training): ",
    print >>f, log_predictive_bayes_lin_reg(training_data,blr)/training_data['design_matrix'].shape[0]
    print >>f, "The average log predictive (testing) : ",
    print >>f, log_predictive_bayes_lin_reg(testing_data,blr)/testing_data['design_matrix'].shape[0]
    BAYES_pred = np.dot(testing_data['design_matrix'],blr['w_N'])
    print >>f, "MSE (testing) : ",
    print >>f, eformat( np.mean( (testing_data['y_noisy'] - BAYES_pred)**2 ), 1, 1)
    print >>f, "MAE (testing) : ",
    print >>f, eformat( np.mean( np.abs(testing_data['y_noisy'] - BAYES_pred) ), 1, 1)
    print >>f, " "


  num_bt = 25
  blr_bt = {}
  raw_log_pred_results = np.zeros((num_bt,2))
  ave_log_pred_results = np.zeros((num_bt,2))
  for i in range(num_bt):
    blr = bayes_linear_reg_analytic_bt(training_data, g=my_G)

    blr_bt[i] = blr

    raw_log_pred_results[i,0] = log_predictive_bayes_lin_reg(training_data,blr)
    ave_log_pred_results[i,0] = log_predictive_bayes_lin_reg(training_data,blr)/training_data['design_matrix'].shape[0]

    raw_log_pred_results[i,1] = log_predictive_bayes_lin_reg(testing_data,blr)
    ave_log_pred_results[i,1] = log_predictive_bayes_lin_reg(testing_data,blr)/testing_data['design_matrix'].shape[0]

  mci_weights = np.exp(raw_log_pred_results[:,0])
  mci_weights /= np.sum(mci_weights)


  print >>f, "MAP"
  print >>f, "The average log predictive (training): ",
  print >>f, np.max(ave_log_pred_results, axis=0)[0]
  map_index = np.argmax(ave_log_pred_results, axis=0)[0]
  print >>f, "The average log predictive (testing) : ",
  print >>f, ave_log_pred_results[map_index,1]
  MAP_pred = np.dot(testing_data['design_matrix'],blr_bt[map_index]['w_N'])
  print >>f, "MSE (testing) : ",
  print >>f, eformat( np.mean( (testing_data['y_noisy'] - MAP_pred)**2 ), 1, 1)
  print >>f, "MAE (testing) : ",
  print >>f, eformat( np.mean( np.abs(testing_data['y_noisy'] - MAP_pred) ), 1, 1)
  print >>f, " "

  pred_bt = np.zeros((num_bt, total_num-num_for_train))
  for i in range(num_bt):
    pred_bt[i,:] = np.dot(testing_data['design_matrix'],blr_bt[i]['w_N']).T
  weighted_pred = mci_weights.dot(pred_bt)

  print >>f, "WEIGHTED"
  print >>f, "The average log predictive (training): ",
  print >>f, mci_weights.dot(ave_log_pred_results)[0]
  print >>f, "The average log predictive (testing) : ",
  print >>f, mci_weights.dot(ave_log_pred_results)[1]
  print >>f, "MSE (testing) : ",
  print >>f, eformat( np.mean( (testing_data['y_noisy'] - weighted_pred)**2 ), 1, 1)
  print >>f, "MAE (testing) : ",
  print >>f, eformat( np.mean( np.abs(testing_data['y_noisy'] - weighted_pred) ), 1, 1)
  print >>f, " "
  with printoptions(precision=3, suppress=True, strip_zeros=False):
    print >>f, "The WEIGHTED weights: ",
    print >>f, mci_weights.T
    print >>f, "The log predictives weights: "
    print >>f, ave_log_pred_results

  # Close file, reopen to read, print to stdout
  f.close()
  f = open(log_filename,'r')
  print f.read()
  f.close()

if __name__ == '__main__':
  main()


