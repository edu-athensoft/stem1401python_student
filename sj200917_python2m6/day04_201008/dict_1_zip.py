"""
Dictionary
zip()
# expected result
{
    1: 'v1',
    2: 'v2',
    3: 'v3',
    4: 'v4'
}
"""
list1 = [1,2,3,4]
list2 = ['v1','v2','v3','v4']

# solution 1.
print("=== solution 1 ===")
mydict = {}

for i in range(4):
    # print(list1[i],list2[i])
    mydict[list1[i]] = list2[i]

print(mydict)
print()


# solution 2
print("=== solution 2 ===")
result = zip(list1, list2)
print(result, type(result))

mydict = dict(result)
print(mydict)


# solution 3
print(dict(zip(list1, list2)))

mydict = dict(zip(list1, list2))




