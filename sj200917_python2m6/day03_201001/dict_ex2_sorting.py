"""
Question:
Write a program to sort a dictionary by key
in both ascending and descending order.

"""

d = {'ca': 2, 'ab': 4, 'bb': 3, 'b': 1, 'aa': 0}

# youran
d_but_sorted = dict(sorted(d.items()))
print(d_but_sorted)

print()

d_but_sorted_in_reverse = dict(sorted(d.items(), reverse=True))
print(d_but_sorted_in_reverse)


# leon li
dt = d.items()

dtd = dict(sorted(dt))
dtt = sorted(dt, reverse=True)
print(dtd, type(dtd), dtt)
