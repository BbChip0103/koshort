.. koshort documentation master file, created by
   sphinx-quickstart on Wed Apr 25 18:43:02 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Koshort: Korean trends streaming in python
==========================================

.. image:: https://travis-ci.org/koshort/koshort.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/koshort/koshort

.. image:: https://readthedocs.org/projects/koshort/badge/?version=latest
    :alt: Documentation Status
    :target: http://koshort.readthedocs.io/en/latest/?badge=latest

Koshort is a Python package for Korean internet trends streaming and processing... or maybe abbreviation of Korean domestic cat.

For step-by-step instructions, follow the :ref:`guide`.
For specific descriptions of each module, go see the api documents.

Lowering the barrier to the domain specific internet corpus
-----------------------------------------------------------

Social network services and other internet communities are open and rich data source of human spoken language.
But due to the issues of privacy and policy of the each websites, sharing bunch of retrieved text data is normally prohibited.
To solve the most major Natural Language Processing (NLP) problem under this circumstances, researchers had to rely on limited public datasets and data brought by their company.
Otherwise they would implement their domain specific crawler for each cases.

Koshort is hardly inspired by the project `KoNLPy <http://konlpy.org>`_, with similar philosphy. It is not about recreating another crawler but to unify efforts around so that anyone can accelerate their projects.


.. sourcecode:: python

    >>> from koshort.stream import NaverStreamer
    >>> streamer = NaverStreamer()
    >>> streamer.stream()
    cj채용
    온주완의 뮤직쇼
    유상무
    현대차
    ...


License
-------

Koshort is Open Source Software, and is released under the license below:

- `GPL v3 or above <http://gnu.org/licenses/gpl.html>`_

User guide
----------

.. toctree::
  :glob:
  :maxdepth: 2

  streamer
  examples

API
---

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   koshort


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
