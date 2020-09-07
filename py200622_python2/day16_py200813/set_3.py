"""
Set is mutable
how to change a set

index is not supported

add() - add one item into a set
update() - add multiple items into a set
"""


# case 1. add()
set1 = {4,7,2}
set1.add(5)
print(set1)
print()

# case 2. update()
set1 = {4,7,2}
print(set1)
set1.update([3,5,9])
print(set1)

set1.update([31,51,91],{67,45},(77,88))
print(set1)



