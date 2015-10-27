#A Probabilistic Model for Using Social Networks in Personalized Item Recommendation
##by Allison J.B. Chaney, David M. Blei, and Tina Eliassi-Rad, RecSys 2015.

Abstract
--------

Preference-based recommendation systems have transformed
how we consume media. By analyzing usage data, these methods
uncover our latent preferences for items (such as articles
or movies) and form recommendations based on the behavior 
of others with similar tastes. But traditional
preference-based recommendations do not account for the 
social aspect of consumption, where a trusted friend might
point us to an interesting item that does not match our 
typical preferences. In this work, we aim to bridge the gap 
between preference- and social-based recommendations. We
develop social Poisson factorization (SPF), a probabilistic
model that incorporates social network information into a
traditional factorization method; SPF introduces the social
aspect to algorithmic recommen- dation. We develop a scalable
algorithm for analyzing data with SPF, and demonstrate that
it outperforms competing methods on six real-world datasets;
data sources include a social reader and Etsy.


Paper
-----

The paper is available from: 

https://github.com/Blei-Lab/Publications/blob/master/2015_ChaneyBleiEliassi-Rad/2015_ChaneyBleiEliassi-Rad.pdf

And from ACM:

http://dl.acm.org/citation.cfm?id=2800193

The citation for this paper is:

```
@inproceedings{Chaney2015,
    author = {Chaney, Allison J.B. and Blei, David M. and Eliassi-Rad, Tina},
    title = {A Probabilistic Model for Using Social Networks in Personalized Item Recommendation},
    booktitle = {RecSys},
    year = {2015},
    isbn = {978-1-4503-3692-5},
    pages = {43--50},
}
```

Code
----

The C/C++ for SPF is available from:
https://github.com/ajbc/spf

And its project page is here:
http://ajbc.io/spf/

Paper Source
------------

Source of the paper is in tex/

All figures from the paper are available from fig/. The raw data used to
generate figures that contain experimental results are in fig/dat/. They
can be generated using the R-scripts in fig/src/.
