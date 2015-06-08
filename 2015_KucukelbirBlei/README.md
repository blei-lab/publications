# Population Empirical Bayes
## Alp Kucukelbir and David Blei, UAI 2015.

Abstract
--------

Bayesian predictive inference analyzes a dataset to make predictions about new
observations. When a model does not match the data, predictive accuracy suffers.
We develop population empirical Bayes (POP-EB), a hierarchical framework that
explicitly models the empirical population distribution as part of Bayesian
analysis. We introduce a new concept, the latent dataset, as a hierarchical
variable and set the empirical population as its prior. This leads to a new
predictive density that mitigates model mismatch. We efficiently apply this
method to complex models by proposing a stochastic variational inference
algorithm, called bumping variational inference (BUMP-VI). We demonstrate
improved predictive accuracy over classical Bayesian inference in three models:
a linear regression model of health data, a Bayesian mixture model of natural
images, and a latent Dirichlet allocation topic model of scientific documents.


Paper
-----

The paper is available from:

https://github.com/Blei-Lab/Publications/blob/master/2015_KucukelbirBlei

Code
----

The C++ for BUMP-VI is available from:
https://github.com/Blei-Lab/lda-bump-cpp

Paper Source
------------

Source of the paper is in tex/

Code for the simulation and the bodyfat example are available in code/.
