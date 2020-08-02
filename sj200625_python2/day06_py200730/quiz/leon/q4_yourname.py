

list4 = [1, 2, 3, 2, 4, 10]
# x = 100
x = list4[0]

for i in list4:
    if x <= i:
        pass
    else:
        if x >= i:
            x = i
            list4.append(i)
print(x)






