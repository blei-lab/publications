"""Bayesian linear regression (analytic solution)

  This program follow the notation and approach of (Murphy, 2012)
  [Chapter 7.6.3] with conjugate priors.

  Prior on weights is a multivariate Normal (N)
  - mean: w_0
  - covariance: V_0

  Prior on variance is Inverse Gamma (IG)
  - shape: a_0
  - scale: b_0

  Joint Prior is NIG

  Joint Posterior is also Normal Inverse Gamma (NIG)

  Posterior marginal of the weights is Student-t
  Posterior marginal of the variance is IG

"""

from time import time
import numpy as np
import matplotlib.pyplot as plt

def bayes_linear_reg_analytic(training_data,
                              w_0=None, V_0=None, a_0=1e-3, b_0=1e-3, g=0.0):

  tStart = time()

  # Get training data
  X = training_data['design_matrix']
  y = np.atleast_2d(training_data['y_noisy']).T
  N = y.size

  # Check prior parameters
  #   if none provided, default to Zellner's g-prior with unit information
  if g == 0.0:
    g = N

  if w_0 != None:
    assert w_0.shape == (X.shape[1], 1)
  else:
    w_0 = np.zeros([X.shape[1],1])

  if V_0 != None:
    assert V_0.shape == (X.shape[1], X.shape[1])
  else:
    V_0 = g * np.linalg.inv(np.dot(X.T, X))

  # Calculate parameters of the posterior (Eqs 7.70-7.73)
  V_0_inv = np.linalg.inv(V_0)
  V_N     = np.linalg.inv(V_0_inv + np.dot(X.T, X))
  w_N     = np.dot(V_N, np.dot(V_0_inv, w_0) + np.dot(X.T, y))
  a_N     = a_0 + N/2.0
  b_N     = b_0 + 0.5 * (
            np.dot(w_0.T, np.dot(V_0_inv, w_0)) +
            np.dot(y.T, y) -
            np.dot(w_N.T, np.dot(np.linalg.inv(V_N), w_N))
            )

  m, s = divmod(time() - tStart, 60)

  return {'w_N':w_N,
          'V_N':V_N,
          'a_N':a_N,
          'b_N':b_N
         }
