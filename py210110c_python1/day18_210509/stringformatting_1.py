"""
String formatting

f-string

Syntax:
str = f'xxxxxx{}xxx xx{}xx xxxx xxx{}xxx'

'xxxxxx{}xxx xx{}xx xxxx xxx{}xxx'.format(v1, v2, v3,...)

hard code
a formatted string returns a string 

"""


width = 20
height = 30
depth = 40

# print out a box dimension
str1 = f'The dimension of the box is like width: {width}inches , height: {height}inches, depth: {depth}inches.'
print(str1, type(str1))


unit = 'inches'
# print out a box dimension
str1 = f'The dimension of the box is like width: {width}{unit} , height: {height}{unit}, depth: {depth}{unit}.'
print(str1)
