#Dynamic Poisson factorization
##by Laurent Charlin, Rajesh Ranganath, James McInerney and David Blei, Rec'Sys 2015.

Abstract
--------

Models for recommender systems use latent factors to explain the
preferences and behaviors of users with respect to a set of items (e.g.,
movies, books, academic papers). Typically, the latent factors are assumed
to be static and, given these factors, the observed preferences and
behaviors of users are assumed to be generated without order. These
assumptions limit the explorative and predictive capabilities of such
models, since users’ interests and item popularity may evolve over time.
To address this, we propose dPF, a dynamic matrix factorization model
based on the recent Poisson factorization model for recommendations. DPF
models the time evolving latent factors with a Kalman filter and the
actions with Poisson distributions. We derive a scalable variational
inference algorithm to infer the latent factors. Finally, we demonstrate
dPF on 10 years of user click data from arXiv.org, one of the largest
repository of scientific papers and a formidable source of information
about the behavior of scientists. Empirically we show performance
improvement over both static and, more recently proposed, dynamic
recommendation models. We also provide a thorough exploration of the
inferred posteriors over the latent variables.

Paper
-----

The paper is available from: 

https://github.com/Blei-Lab/Publications/blob/master/2015_CharlinRanganathMcInerneyBlei/2015_CharlinRanganathMcInerneyBlei.pdf

Code
----

The C/C++ for dPF is available from:
https://github.com/Blei-Lab/dPF

Paper Source
------------

Source of the paper is in tex/

All figures from the paper are available from fig/.
