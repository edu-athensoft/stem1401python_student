"""
Quiz 5
"""
# 6.2
list1 = [1, 2, 3, 4, 5, 6]
print(list1[0], list1[5])
# 1 6

# 6.3
list1[3] = 999

# 6.4
tuple1 = (1, 2, 3, 4, 5, 6)
print(tuple1[0], tuple1[5])
# 1 6

# 6.5
answer = "b"

# 6.6
set1 = {1, 1, 2, 2, 3, 3}
print(set1)
# {1,2,3}

# 6.7
dict1 = {"Y": "Yes",
         "N": "No"
         }
print(dict1)
# {'Y': 'Yes', 'N': 'No'}

# 7.
# float -> string
float1 = 1.1
str1 = str(float1)

# string -> integer
# str2 = "asdf"
# int1 = (int(str2)
# ValueError
# error if it contains literals that are not digits

str3 = "123"
print(int(str3))
# 123
