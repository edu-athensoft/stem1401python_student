"""
Summary of tuple

there are certain advantages of implementing a tuple over a list.
Below listed are some of the main advantages:

1. We generally use tuples for heterogeneous (different) data types and
lists for homogeneous (similar) data types.

2. Since tuples are immutable, iterating through tuples is faster than with lists.
So there is a slight performance boost.

3. Tuples that contain immutable elements can be used as a key for a dictionary.
With lists, this is not possible.

4. If you have data that doesn't change, implementing it as tuple will
guarantee that it remains write-protected.

"""
