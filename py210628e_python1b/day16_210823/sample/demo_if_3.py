"""
condition of if

what can be a condition?
1. boolean value/literal
2. comparision expression  (returns boolean value)
3. logical expression

4. primitive type (int, float, string)
5. collection type (list, tuple, set, dict)
"""

# case 10.
print("=== case 10. ===")
mylist = ['a','b','c']

if mylist:
    print("A not empty list can be as True")


# case 11.
print("=== case 11. ===")
emptylist = []
if emptylist:
    print("An empty list can be as False")
else:
    print("An empty list can be as False")


# delete an item from a list
print("remove items one by one")
mylist.pop()
print(mylist)

mylist.pop()
print(mylist)

mylist.pop()
print(mylist)

