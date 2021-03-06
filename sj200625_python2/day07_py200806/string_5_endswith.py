"""
endswith()

The endswith() method returns True if a string
ends with the specified suffix. If not, it returns False.

str.endswith(suffix[, start[, end]])
"""

# Example 1
text = "Python is easy to learn."

result = text.endswith('to learn')
print(result)

result = text.endswith('to learn.')
print(result)

result = text.endswith('Python is easy to learn.')
print(result)
print()

# Example 2
text = "Python programming is easy to learn."

# start parameter: 7
result = text.endswith('learn.', 7)
print(result)

result = text.endswith('easy', 7, 26)
# returns True
print(result)
print()

# Example 3
text = "programming is easy"
result = text.endswith(('programming', 'python'))
print(result)

result = text.endswith(('programming', 'python', 'easy'))
print(result)