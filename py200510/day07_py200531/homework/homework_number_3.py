def word(a,y):
    b = []
    c = y.split(" ")
    for i in c:
     if len(i) > a:
        b.append(i)
    return b
x = ('The python homework number three')
print(word(4,x))

