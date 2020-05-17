"""
filter()

mylist1 = [1,2,3,4,5,6,7,8,9,10]
even number
expect result = [2,3,4,8,10]
"""''

mylist1 = [1,2,3,4,5,6,7,8,9,10]
print("The original list is: ",mylist1)
result = []

for i in mylist1:
    if i % 2 == 0:
        result.append(i)

print("The result is: ", result)


# using lambda function with filter()
print(list(filter(lambda x: x%2 == 0,  mylist1)))



