Outline
=======

2.1 What is up with levels?
---------------------------

Our mind works like a zoom lens on a camera.
We move in and out of ranges of detail and shift our focus about what matters.

2.1.1 Mid Level – Home Court
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is where you write code that gets a job done.
It is what most people think of when the say, "I write code".

The essential skills here are:

* Knowing the core language of Python (think with-statements and for-loops).
* Knowing what is in your libraries (think itertools, numpy, and Pandas)
* Knowing some patterns for how those pieces fit together.

You get good at this by taking training, reading documentation, and practice.

Large language models are starting to do a good job at this level by training on published examples.
In the future, I think you will mainly need this skill to review code written by an LLM.

2.1.2 Low Level – The Underground
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the level where you know what your machine is thinking about.
Do you know how things work?

Here are some examples of knowledge at this level:

* Sets do not define a total ordering so extra care is needed if you need to sort a list of sets.
  ``sorted(list_of_sets, key=sort)``

* The in-operator for strings does a linear search for substring matches.
  ``"connected" in device_status`` matches BOTH ``"Status: connected"`` and ``"Status: disconnected"``.

* The in-operator for sets is scale invariant but depends on how equality is defined (typically exact matches) and a corresponding hash method (usually not for mutable objects).

People who enjoy programming tend to gather some of this information over time. You also get it by talking to people who really love programming or by attending conferences.

Otherwise, most people don't go underground unless they have to.

Large language models excel at looking up low level explanations. Likely, they have been trained on StackOverflow explanations.

But critically, LLMs don't know what those explanations mean, recognize them where they matter, or be able from a place of understanding.

The winning marriage here is getting an LLM to explain what code is doing under the hood and then we can take it from there.

2.1.3 High Level – The Problem Domain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the level where you become super productive and can think big thoughts without becoming lost in detail.

Letting code teach you how to make reusable functions is an easily learned skill. However, most people can't be bothered. They spend much of the lives retyping variations of the same code. (I say "they" but we all do it to some degree.)

A much more challenging task is to consciously implement an ontology from the problem domain.

This is all about making the program fit the problem instead of the other way around.

Interestingly, domain experts tend to do this naturally but traditional programmer struggles with it.

Air traffic controller:

* Switch active runways
* Maintain separation


Programmer:

* Order descent, climb, or level
* Change heading
* Alter airspeed

I've not seen an LLM be able to create a good high level API but for unfamiliar problem domains, LLMs can teach us the ontology, how to "talk the talk". This can help us create APIs which the LLMs can then code.

2.1.4 Where we are going
^^^^^^^^^^^^^^^^^^^^^^^

Here's my plan:

* There is no big message.
* I will show you a little code that I've found interesting.
* Think about which level we are coding.
* Consider how an LLM would help or hinder.
* It is food for thought.
