Sparrow Python SDK
==================

The Sparrow Python SDK provides convenient access to the Sparrow API
from applications written in the Python language. It includes a
pre-defined set of classes for API resources that initialize themselves
dynamically from API responses which makes it compatible with a wide
range of versions of the Sparrow API.

Installation
------------

Python 2.7+ or 3.4+ is required.

::

    pip install --upgrade sparrowone

Usage
-----

To make requests, you first need to create a Connection instance:

.. code:: py

    import sparrowone

    # You can find your Merchant keys in your Sparrow account
    sprw = sparrowone.Connection(m_key="MTA6MzM6NTYgUE0tLVBheVRhY3RpeALO")
    sprw.sale(
        9.95,
        sparrowone.CardInfo(
            number="4111111111111111",
            expiration="1013",
            cvv="999"
        )
    )

See the `API docs`_ for more advanced examples.

.. _API docs: http://foresight.sparrowone.com/

Development
-----------

We use the builtin `unittest`_ module for tests. To run all tests::

    python -m unittest discover

Or, if you want to run a specific test file, try this::

    python -m unittest discover -vp test_sale.py

We run tests against Python versions 2.7 and 3.5 for now.

.. _unittest: https://docs.python.org/3/library/unittest.html
