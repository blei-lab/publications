# The Variational Gaussian Process
## Dustin Tran, Rajesh Ranganath, and David M. Blei, ICLR 2016

Abstract
--------

Variational inference is a powerful tool for approximate inference, and it has been recently applied for representation learning with deep generative models. We develop the variational Gaussian process (VGP), a Bayesian nonparametric variational family, which adapts its shape to match complex posterior distributions. The VGP generates approximate posterior samples by generating latent inputs and warping them through random non-linear mappings; the distribution over random mappings is learned during inference, enabling the transformed outputs to adapt to varying complexity. We prove a universal approximation theorem for the VGP, demonstrating its representative power for learning any model. For inference we present a variational objective inspired by auto-encoders and perform black box inference over a wide class of models. The VGP achieves new state-of-the-art results for unsupervised learning, inferring models such as the deep latent Gaussian model and the recently proposed DRAW.

Paper
-----

The paper is available from:

https://github.com/Blei-Lab/Publications/blob/master/2016_TranRanganathBlei

The citation for this paper is:

```
@inproceedings{tran2016variational,
  author = {Tran, Dustin and Ranganath, Rajesh and Blei, David M.},
  title = {The Variational Gaussian Process},
  booktitle = {International Conference on Learning Representations},
  year = {2016}
}
```

Paper Source
------------

Source of the paper is in `tex/`.

All figures from the paper are available from `fig/`.
