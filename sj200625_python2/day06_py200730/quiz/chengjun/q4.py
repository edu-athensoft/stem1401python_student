list = [1, 2, 20, 3, 2, 4, 16, 15]
a=20
for b in list:
    if a <= b:
        pass
    else:
        if a >= b:
            a = b
            # list.append(b)
        elif a == b:
            # list.append(b)
            pass
print(a)