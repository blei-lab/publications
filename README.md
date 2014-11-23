## Description
============

This repo contains papers published in the [Blei Lab](http://www.cs.columbia.edu/~blei/). 

Our aim is reproducibility: when possible, the code and data used to generate the figures is included too. 

This repo contains a list of folders, with one folder for each paper. Folders are labeled "YYYY_LastNames". For example, the folder "2014_GopalanCharlinBlei" contains everything associated with the "Content-based recommendation with Poisson factorization" paper in NIPS 2014 with authors P. Gopalan, L. Charlin, and D.M. Blei.

In the root of each folder, the README.txt file contains a description of the folder contents - if the paper is associated with
software, such as an open-source package, it will be pointed to here and on [the main organization page](https://github.com/Blei-Lab) as well as this README. 

The pdf file in the root of each folder in the repo is the paper generated from the LaTeX files in /tex (using any style files in /tex/sty).

Scripts for generating the figures used in the paper are in the /fig/src directory, while the data used for the figures is in /fig/dat, and the final figures used are in /fig/pdf (which might have been tweaked in Adobe Illustrator).

In summary, here is the folder naming structure of each paper in this repo:
 * YYYY_LastNames/README.txt (a description of what is in the folder)
 * YYYY_LastNames/YYYY_LastNames.pdf (the paper)
 * YYYY_LastNames/YYYY_LastNames.bib (bib entry for the paper)
 * YYYY_LastNames/fig/src (Python/R scripts to make figures)
 * YYYY_LastNames/fig/dat (data used in figures)
 * YYYY_LastNames/fig/pdf (final figures)
 * YYYY_LastNames/tex (LaTeX source files)
 * YYYY_LastNames/tex/sty (any LaTeX style files used)

Blei Lab internal notes: If the paper includes an open-source package, make a separate repo for the code from your account, and fork it into the Blei Lab github organization. You can make your code citable and get a DOI by following this: https://guides.github.com/activities/citable-code/
