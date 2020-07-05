"""
eval()

evaluate a string of expression

1+2
3*5
4/6 + 2
"""

# case 1.
r1 = eval("1+2")
print("1+2 =", r1)

# case 2.  3x5
r2 = eval("3*5")
print("3*5 =", r2)

# case 3. 4/6 +2
r3 = eval("4/6 + 2")
print("4/6+2 =", r3)



# using input
expr1 = input("Enter an arithmetic expression:")
result = eval(expr1)
print("The result is", result)