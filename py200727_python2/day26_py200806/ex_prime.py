"""

"""

# kevin

count = 0

list1 = list(range(5,21))
# print(list1)

for a in list1:
    for i in range(2,a):
        if a % i == 0:
            break
        else:
            print(a)
            count += 1
            break

print("there are {} prime numbers".format(count))
