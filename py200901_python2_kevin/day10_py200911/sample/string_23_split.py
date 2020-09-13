"""
split()

breaks up a string at the specified separator and returns a list of strings.

str.split([separator [, maxsplit]])
str.split()
"""

# Example 1.
mytext = "Python \n is  an awesome \t language"

result = mytext.split()
print(result)

# Example 2.
mytext = "Python is an awesome language"

result = mytext.split()
print(result)


# Example 3.
grocery = 'Milk, Chicken, Bread'
print(grocery.split(', '))

print(grocery.split(','))
print(grocery.split(':'), len(grocery.split(':')))
print("=====")

# strip()


# Example 4.
mytext = "Python is an awesome language"

result = mytext.split(' ', 1)
print(result)

result = mytext.split(' ', 2)
print(result)

result = mytext.split(' ', 0)
print(result)

result = mytext.split(' ', 5)
print(result)