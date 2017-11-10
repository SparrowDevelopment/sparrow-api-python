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

    pip install --upgrade sparrow

Usage
-----

To make requests, you first need to create a Connection instance:

.. code:: py

    import sparrow

    # You can find your Merchant keys in your Sparrow account
    sprw = sparrow.Connection(m_key="MTA6MzM6NTYgUE0tLVBheVRhY3RpeALO")
    sprw.sale(
        9.95,
        sparrow.CardInfo(number="4111111111111111",
                         expiration="1013",
                         cvv="999")
    )

See the `API docs`_ for more advanced examples.

.. _API docs: http://foresight.sparrowone.com/
