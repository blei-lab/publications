## Description

This repo contains papers published in the [Blei Lab](http://www.cs.columbia.edu/~blei/). 

Our aim is reproducibility: when possible, the code and data used to generate the figures is included too. 

This repo contains a list of folders, with one folder for each paper. Folders are labeled `YYYY_LastNames/`. For example, the folder `2014_GopalanCharlinBlei/` contains everything associated with the "Content-based recommendation with Poisson factorization" paper in NIPS 2014 with authors P. Gopalan, L. Charlin, and D.M. Blei.

Here is the directory structure for each paper:
 * `YYYY_LastNames/README.md`: a brief description and a link to any associated software
 * `YYYY_LastNames/YYYY_LastNames.pdf`: the paper
 * `YYYY_LastNames/YYYY_LastNames.bib`: bib entry to cite the paper
 * `YYYY_LastNames/fig/src`: Python/R scripts to make figures
 * `YYYY_LastNames/fig/dat`: data used in figures
 * `YYYY_LastNames/fig/pdf`: final figures
 * `YYYY_LastNames/tex`: LaTeX source files
 * `YYYY_LastNames/tex/sty`: any LaTeX style files used

Blei Lab internal notes: If the paper includes an open-source package, make a separate repo for the code from your account, and fork it into the Blei Lab github organization. You can make your code citable and get a DOI by following this: https://guides.github.com/activities/citable-code/
