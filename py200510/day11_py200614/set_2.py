"""
change a set, adding elements

add()
update()

"""


set1 = {1,3}
print(set1)

# proved that set is mutable
set1.add(2)
print(set1)

print()
# cannot prove that set is mutable
# set2 = set1.add(2)
# print(set2)

# update()
print("=== update() ===")
set1 = {1,3}
print(set1)
# *s: Iterable[_T]
set1.update([4,5,6])
print(set1)

set1.update([7,8],[9,10])
print(set1)

set1.update([3, 81], (1, 100))
print(set1)

# access item of a set
# TypeError: 'set' object does not support indexing
# set1[0]


# def foo(*objects):
#     pass

set1 ={'a','b','c'}
print(set1)

set1 ={1,2,3}
print(set1)





