"""
1. naming for identifier
function
string
sum()
set

2.why using set()

str1
mystring
xxx_str
str_
"""


def function(set):
   if len(set) == 0:
      return []
   if len(set) == 1:
      return [set]
   b = []
   for i in range(len(set)):
      c = set[i]
      a = set[:i] + set[i + 1:]
      for y in function(a):
         b.append([c] + y)
   return b

string = list(input('Please enter a string:'))

result = []
for y in function(string):
   # print(y)
   if y not in result:
      result.append(y)
      print(y)


# print(result)
