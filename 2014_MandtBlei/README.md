### Smoothed Gradients for Stochastic Variational Inference
#### by Stephan Mandt and David Blei, NIPS 2014.  

ABSTRACT

Stochastic variational inference (SVI) lets us scale up Bayesian computation to massive data. It uses stochastic optimization to fit a variational distribution, following easy-to-compute noisy natural gradients. As with most traditional stochastic optimization methods, SVI takes precautions to use unbiased stochastic gradients whose expectations are equal to the true gradients. In this paper, we explore the idea of following biased stochastic gradients in SVI. Our method replaces the natural gradient with a similarly constructed vector that uses a fixed-window moving average of some of its previous terms. We will demonstrate the many advantages of this technique. First, its computational cost is the same as for SVI and storage requirements only multiply by a constant factor. Second, it enjoys significant variance reduction over the unbiased estimates, smaller bias than averaged gradients, and leads to smaller mean-squared error against the full gradient. We test our method on latent Dirichlet allocation with three large corpora.

PAPER

- 2014_MandtBlei.pdf

SCRIPTS FOR PLOTTING DATA

- open the plot scripts in /fig/src with "ipython notebook --pylab" (a browser window will pop up).



DATA FILES

- meaning of the columns of the data files that begin with "ARX_BIAS_VAR_...":
  0: iterations, 1: run time in hours, 2: held-out likelihood, 3: to be ignored, 4: squared bias, 5: variance, 6: squared error.

- columns in all other data files (without "BIAS_VAR"):
  0: iterations, 1: run time in hours, 2: held-out likelihood, 3: to be ignored. 
