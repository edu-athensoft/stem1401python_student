"""
break and continue

break and continue statements can alter the flow of a normal loop.


break statement

the break statement terminate the loop containing it.
Control of the program flows to the statement immediately after the body of the loop.

If break statement is  inside a nested loop, break will terminate the innermost loop.

"""

"""
break
"""

# 1,2,3,4,5,6,7,8

for num in [1,2,3,4,5,6,7,8]:
    print(num)
print()

for num in [1,2,3,4,5,6,7,8]:
    if num == 6:
        break
    print(num)
print()

for num in [1,2,3,4,5,6,7,8]:
    print(num)
    if num == 6:
        break