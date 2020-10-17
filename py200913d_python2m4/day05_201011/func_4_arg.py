"""
function
python arbitrary arguments
"""

print()
print(1)
print(1,'abc')
print(1,'abc',True)
print()
print()

def greet(*names):
    # print(names, type(names))
    for name in names:
        print(name)
    print("greeting")

greet('f1','f2','f3')
print()
print()
greet('f1','f2','f3','f4','f5')
print()
print()
greet()

