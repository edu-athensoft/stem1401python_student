"""
filter()

original list of number is [1,2,3,4,5,6,7,8,9,10]
pick up every even number in order
output the new list
"""

original_list = [1,2,3,4,5,6,7,8,9,10]
print(original_list)

a = filter(lambda x: x%2==0, original_list)
# print(a, type(a))

# covert to a list which can be read
print(list(a))

# in compact style
print(list(filter(lambda x: x%2==0, original_list)))
print()




# method2: for-loop
result = []
for i in original_list:
    if i%2 == 0:
        result.append(i)

print("Filtered list is {}".format(result))
