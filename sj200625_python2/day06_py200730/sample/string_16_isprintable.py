"""
string isprintable()

Characters that occupy printing space on the screen are known as printable characters

digits
alphabet (letters and symbols)
punctuations
whitespace
"""

# case 1.
str1 = 'Space is a printable'
print(str1)
print(str1.isprintable())
print()

# case 2.
str1 = '\nNew Line is printable'
print(str1.isprintable())
print()

# case 3.
str1 = " "
print(str1.isprintable())
print()

# case 4.
str1 = ''
print(str1.isprintable())
print()

# case 5.
# written using ASCII
str1 = chr(27) + chr(97)

if str1.isprintable():
  print('Printable')
  print(str1)
else:
  print('Not Printable')
print()

str1 = '3+3=6'
if str1.isprintable():
  print('Printable')
  print(str1)
else:
  print('Not Printable')