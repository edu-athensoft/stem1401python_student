"""
slicing

"""

# ex.
words = 'Python is a good programming language.'

words = ['p','y','t','h','o','n']

# case 1. slicing from the index of 0
print("=== case 1 ===")
result = words[0:1]
print(result)

result = words[0:2]
print(result)

# ex.
result = words[0:4]
print(result)

result = words[:4]
print(result)
print()


# case 2. slicing to the last item/index
print("=== case 2 ===")
result = words[2:6]
print(result)

result = words[2:]
print(result)
print()


# case 3. slicing from A to B
print("=== case 3 ===")
result = words[2:4]
print(result)
print()


# case 4. slicing all items
print("=== case 4 ===")
result = words[0:len(words)]
print(result)

result = words[:]
print(result)





