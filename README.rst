is_sorted
=========

*is_sorted* is a tiny Python tool to check if list (or any iterable) is sorted.

Installation
------------

.. code-block:: console

    pip install is_sorted


Examples
--------

.. code-block:: python

   >>> from is_sorted import is_sorted
   >>> is_sorted([1, 2, 3, 4, 5, 6])
   True
   >>> is_sorted([1, 3, 2, 0])
   False
   >>> is_sorted([5, 4, 3, 2, 1], reverse=True)
   True
   >>> is_sorted([(1, 2), (2, 0), (3, 10), (3, 9), (4, 5)], key=lambda x: x[0])
   True