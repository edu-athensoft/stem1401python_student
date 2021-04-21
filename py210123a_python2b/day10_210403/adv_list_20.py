"""
list comprehension

expression of filter

"""

# pick up odd numbers and create a new list
# double each selected number

list2 = [1,2,3,4,5,6,7,8]

# expected result: [2,6,10,14]
result = [2*i for i in list2]
print(result)

result = [2*i for i in list2 if i%2==1]
print(result)

result2 = [2*i for i in list2 if i>=5]
print(result2)

list3 = []
for i in list2:
    if i>5:
        list3.append(2*i)
