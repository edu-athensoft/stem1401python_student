# for loop

# modulus
# print(5 % 2)


# return list_a whose item are doubled.
"""
1 -> 2
2 -> 3
...
9 -> 10
"""
list_a = [1,2,3,4,5,6,7,8,9]

for x in list_a:
    x = x + 1
    # print out only the even number
    # print(x)
    if x%2 ==0:
        print(x)

print(list_a)
for i in range(0,9):
    list_a[i] = list_a[i] +1

print(list_a)