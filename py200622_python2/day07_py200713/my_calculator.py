"""
Mini project:
v1. do arithmetic operation
    +, -, *, /

v2. upgrade
    add logical operation
    and or not

"""

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

print("=== my calculator ===")


# test
# print(add(1,2))
# print(sub(1,2))


# choose an operation
print("""Arithmetic operation:
1. adding
2. subtracting
""",end='')

operation = int(input("Choose an operation by number:"))
print(operation)

# test menu
# if operation == 1:
#     print(f"[info] operation : {operation}")
# elif operation == 2:
#     print(f"[info] operation : {operation}")
# else:
#     print("[error] No such or invalid operation")

input1 = int(input("input1:"))
input2 = int(input("input2:"))

if operation == 1:
    print(f"{input1} + {input2} = {add(1,2)}")
elif operation == 2:
    print(f"{input1} - {input2} = {sub(1,2)}")
else:
    print("[error] No such or invalid operation")

