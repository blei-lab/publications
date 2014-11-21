Description
============

This repo contains the pdf and LaTeX source for papers published in the [Blei Lab](http://www.cs.columbia.edu/~blei/). 

Our aim is reproducibility: when possible, the code and data used to generate the figures is included too. 

So if you see a figure or LaTeX hack in a paper that you like, feel free to use it!

## Conventions

* Folders for each paper are labeled "YYYY_LastNames". For example, "2014_GopalanCharlinBlei".

* In each folder, both the .pdf and .bib entry are in the root. 

* This is the naming convention we use:
 * YYYY_LastNames/YYYY_LastNames.pdf
 * YYYY_LastNames/YYYY_LastNames.bib
 * YYYY_LastNames/fig/src (R/python scripts to generate figures)
 * YYYY_LastNames/fig/dat (data used to generate figures)
 * YYYY_LastNames/fig/pdf (final figures)
 * YYYY_LastNames/tex (LaTeX source files)
 * YYYY_LastNames/tex/sty (any LaTeX style files used)

* If the paper includes an open-source package, make a separate repo for the code and fork it into the Blei Lab github organization. You can make your code citable and get a DOI by following this: https://guides.github.com/activities/citable-code/
