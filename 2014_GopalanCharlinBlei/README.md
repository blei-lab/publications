#Content-based recommendations with Poisson factorization
##by Prem Gopalan, Laurent Charlin, and David Blei, NIPS 2014.

Abstract
--------

We develop collaborative topic Poisson factorization (CTPF), a
generative model of articles and reader preferences. CTPF can be used
to build recommender systems by learning from reader histories and
content to recommend personalized articles of interest.  In detail,
CTPF models both reader behavior and article texts with Poisson
distributions, connecting the latent topics that represent the texts
with the latent preferences that represent the readers.  This provides
better recommendations than competing methods and gives an
interpretable latent space for understanding patterns of readership.
Further, we exploit stochastic variational inference to model massive
real-world datasets. For example, we can fit CPTF to the full arXiv
usage dataset, which contains over 43 million ratings and 42 million
word counts, within a day.  We demonstrate empirically that our model
outperforms several baselines, including the previous state-of-the art
approach.


Paper
-----

The paper is available from: 

https://github.com/Blei-Lab/Publications/blob/master/2014_GopalanCharlinBlei/2014_GopalanCharlinBlei.pdf

And from the conference website:

http://papers.nips.cc/paper/5360-content-based-recommendations-with-poisson-factorization

Code
----

The C/C++ for CTPF is available from:
https://github.com/premgopalan/collabtm

Paper Source
------------

Source of the paper is in tex/

All figures from the paper are available from fig/. The raw data used to
generate figures that contain experimental results are in fig/dat/. They
can be generated using the R-scripts in fig/src/.
