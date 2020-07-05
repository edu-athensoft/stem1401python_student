"""
3.7 Advantages of Tuple over List
Since tuples are quite similar to lists, both of them are used in similar situations as well.

However, there are certain advantages of implementing a tuple over a list. Below listed are some of the main advantages:

We generally use tuple for heterogeneous (different) datatypes and list for homogeneous (similar) datatypes.
Since tuples are immutable, iterating through tuple is faster than with list. So there is a slight performance boost.
Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

"""
