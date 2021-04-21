"""
list of data type
(group of numbers)
1. int
2. float
3. complex  (ignore)
4. str
5. bool
6. list
7. tuple
8. set
9. dict

"""

# 1. int  (integer)
i = 10
print('The data type of i is',type(i))
print(isinstance(i, int))

# 2. float (floating)
f = 1.5
print('The data type of f is',type(f))
print(isinstance(f, float))

# 3. complex
c = 1+2j
print('The data type of c is',type(c))
print(isinstance(c, complex))

# 4. str  (string)
s = 'abc123'
print('The data type of s is',type(s))
print(isinstance(s, str))

# 5. bool  (boolean)
b = True
print('The data type of b is',type(b))
print(isinstance(b, int))

# 6. list  (list)
list1 = [1,2,3]
print('The data type of list1 is',type(list1))
print(isinstance(list1, list))

# 7. tuple  (tuple)
tuple1 = (1,2,3)
print('The data type of tuple1 is',type(tuple1))
print(isinstance(tuple1, tuple))

# 8. set  (set)
set1 = {1,2,3}
print('The data type of set1 is',type(set1))
print(isinstance(set1, set))

# 9. dict  (dictionary)
dict1 = {1:'1',2:'2',3:'3'}
print('The data type of dict1 is',type(dict1))
print(isinstance(dict1, dict))