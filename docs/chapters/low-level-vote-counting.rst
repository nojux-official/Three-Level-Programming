Low Level – Vote Counting
========================

2.2 Low Level – Vote Counting
-----------------------------

This level is all about understanding what your computer is thinking about.
This is "classical expertise" that comes from training, experience, reading, and attending conferences.

2.2.1 Voting
^^^^^^^^^^^^

Counting votes. How hard could it be?

.. image:: ../_static/images/votes.jpg
   :alt: Description of the image
   :class: my-image-class
   :width: 80%
   :align: center


2.2.2 Baseline Example
^^^^^^^^^^^^^^^^^^^^^^

Given votes in an election, determine the winner:

.. code-block:: python

    winner = max(votes, key=votes.count)

This works fine with a dataset like:

.. code-block:: python

    votes = 'HTTTHHHHTHTTTHHHHHTHHHTTHTTTHHHT'

But what about one like:

.. code-block:: python

    votes = 'HTTTHHHHTHTTTHHHHHTHHHTTHTTTHHHT' * 10_000_000

2.2.3 Breaking it Down
^^^^^^^^^^^^^^^^^^^^^

The overall ballot counting looks like:

.. code-block:: python

    def election(votes):
        return maximum(votes, key=lambda cand: count(votes, cand))

Which is made up of two routines:

.. code-block:: python

    def count(sequence, target):
        result = 0
        for element in sequence:
            if element == target:
                result += 1
        return result

    def maximum(sequence, key):
        max_element = sequence[0]
        max_value = key(max_element)
        for element in sequence:  # <-- A for-loop
            value = key(element)  # <-- Argh, another for-loop
            if value > max_value:
                max_element = element
                max_value = value
        return max_element

This reveals the problem. A for-loop inside a for-loop is quadratic.

2.2.4 A Log Linear Alternative
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sorting and grouping are much faster:

.. code-block:: python

    from itertools import groupby

    def summarize(votes):
        summary = []
        for candidate, ballots in groupby(sorted(votes)):
            summary.append((candidate, len(list(ballots))))
        return summary

The sorting step brings like votes together:

.. code-block:: python

    >>> ''.join(sorted(votes))
    'HHHHHHHHHHHHHHHHHHTTTTTTTTTTTTTT'

The grouping step creates a break for each candidate:

.. code-block:: python

    >>> for candidate, group in groupby(_):
    ...     print(candidate, ''.join(group))
    H HHHHHHHHHHHHHHHHHH
    T TTTTTTTTTTTTTT

2.2.5 Single Pass
^^^^^^^^^^^^^^^^

We can do better by using a dictionary to summarize in a single pass:

.. code-block:: python

    def tabulate(votes):
        tally = {}
        for candidate in votes:
            tally[candidate] = tally.get(candidate, 0) + 1
        return tally

This is approximately what collections.Counter does.
