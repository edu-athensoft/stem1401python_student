
list3 = [1, 2, 3, 2, 4, 10]
x = 0

for i in list3:
    if x >= i:
        pass
    else:
        if x <= i:
            x = i
            list3.append(i)
        elif x == i:
            list3.append(i)
print(x)



