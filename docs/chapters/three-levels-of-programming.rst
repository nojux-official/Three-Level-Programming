Three Levels of Programming
==========================

Presented by Raymond Hettinger

To be excellent, you need to program at three levels:

1. Code that gets the job done
2. Building higher-level abstractions
3. Understanding one layer down, knowing what your tools are doing under the hood

This talk works through many examples to establish patterns for success. You will also gain new insights into what CPython actually does.

Food for thought: What do you think about this snippet of code:

.. code-block:: python

    winner = max(votes, key=votes.count)

