"""
Quiz 5 question 6 answers
"""
# 6.2 define a list with 6 items, then take the first and last one and print them out
l_1 = [1, 2, 3, 4, 5, 6]
print(l_1[0], l_1[-1])
# Output: 1 6

# 6.3 change the value in the [3] position to 999
l_1[3] = 999
print(l_1)
# Output: [1, 2, 3, 999, 5, 6]

# 6.4  define a tuple with 6 items, then take the first and last one and print them out
t_1 = (1, 2, 3, 4, 5, 6)
print(t_1[0], t_1[-1])
# Output: 1 6

# 6.5 can we change the value of a tuple
# Answer: b) No

# 6.6 define a set of {1, 1, 2, 2, 3, 3} what would the result be
s_1 = {1, 1, 2, 2, 3, 3}
print(s_1)
# Output: {1, 2, 3}

# 6.7 define a dictionary with 2 entries and print them out
d_1 = {
    "num1": 23,
    "num2": 54
}
print(d_1)
# Output: {'num1': 23, 'num2': 54}
