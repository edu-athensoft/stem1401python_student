"""
condition of if

what can be a condition?
1. boolean value/literal
2. comparision expression  (returns boolean value)
3. logical expression

4. primitive type (int, float, string)
5. collection type (list, tuple, set, dict)

"""

# case 1.
if True:
    print("test")

if False:
    print("test")


# case 2.
flag = True
if flag :
    print("test")


# case 3.
if 5 > 3:
    print("test")

# case 4.
expr = 5 > 3
if expr:
    print("test")


# case 5.
if 5 > 3 and False:
    print("test")


# case 6.
expr = 5 > 3 and False
if expr:
    print("test")


print("=== case 7. ===")
# case 7.
if 10:
    print("int can be a condition")








