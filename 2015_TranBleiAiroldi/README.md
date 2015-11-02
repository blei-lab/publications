# Copula variational inference
## Dustin Tran, David M. Blei, and Edoardo M. Airoldi, NIPS 2015

Abstract
--------

We develop a general variational inference method that preserves
dependency among the latent variables. Our method uses copulas to
augment the families of distributions used in mean-field and
structured approximations. Copulas model the dependency that is not
captured by the original variational distribution, and thus the
augmented variational family guarantees better approximations to the
posterior. With stochastic optimization, inference on the augmented
distribution is scalable. Furthermore, our strategy is generic: it can
be applied to any inference procedure that currently uses the
mean-field or structured approach. Copula variational inference has
many advantages: it reduces bias; it is less sensitive to local
optima; it is less sensitive to hyperparameters; and it helps
characterize and interpret the dependency among the latent variables.

Paper
-----

The paper is available from:

https://github.com/Blei-Lab/Publications/blob/master/2015_TranBleiAiroldi

The citation for this paper is:

```
@inproceedings{tran2015copula,
  author = {Tran, Dustin and Blei, David M. and Airoldi, Edoardo M.},
  title = {Copula variational inference},
  booktitle = {Neural Information Processing Systems},
  year = {2015}
}
```

Paper Source
------------

Source of the paper is in `tex/`

All figures from the paper are available from `fig/`. The raw data used to
generate figures that contain experimental results are in `fig/dat/`. They
can be generated using the R-scripts in `fig/src/`.
