"""
condition of if

what can be a condition?
1. boolean value/literal
2. comparision expression  (returns boolean value)
3. logical expression

4. primitive type (int, float, string)
5. collection type (list, tuple, set, dict)

"""

print("=== case 7. ===")
print("Integers which are not zero can be taken as True, while 0 can be taken as False")

# case 7.
if 10:
    print("positive int can be a condition")


if -10:
    print("negative int can be a condition")


if 0:
    print("zero can be a condition")
else:
    print("zero cannot be a condition")



print("=== case 8. ===")
# case 8.
if 10.0:
    print("positive float can be a condition")

if -10.0:
    print("negative float can be a condition")

if -0.0:
    print("0.0 float can be True")
else:
    print("0.0 cannot be True")


print("=== case 9. ===")
mystr = 'abc'

if mystr:
    print("a not empty string can be as True")


mystr = ' ' # whitespace is not empty
mystr = ''


if mystr:
    print("a not empty string can be as True")
else:
    print("an empty string can be as False")



