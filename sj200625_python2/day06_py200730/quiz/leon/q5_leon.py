
list1 = ['abc', 'xyz', 'aba', '1221','aa']
x = 0
for i in list1:
    if len(i) >= 2:
        if i[0] == i[-1]:
            x = x + 1

print(x)

