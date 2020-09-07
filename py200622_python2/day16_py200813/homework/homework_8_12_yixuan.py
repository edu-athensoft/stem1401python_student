mylist = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
mylist[4] = mylist[0]
mylist[0] = (2, 1)
print(mylist)
print()


mylist2 = [(2, 5), (1, 2), (2, 5), (4, 5), (2, 3), (1, 2), (2, 1)]
final_list = []
for num in mylist2:
    if num not in final_list:
        final_list.append(num)
print(final_list)
print()

mylist3 = [(2, 5), (1, 2), (2, 5), (4, 5), (2, 3), (1, 2), (2, 1)]

if mylist3 == []:
    print("clear")
else:
    print("not clear")
print()

mylist4 = [(2, 5), (1, 2), (4, 5), (2, 3), (2, 1)]
a = mylist4 * 2
print(a)
print()

mylist5 = [(2, 5), (1, 2), (4, 5), (2, 3), (2, 1)]
if len(mylist5) >= 3:
    print("The quick brown fox jumps over the lazy dog")
else:
    print("small to 3")
print()