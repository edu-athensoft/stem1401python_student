"""
Homework 4 - Kevin
To calculate the n th item of a Fibonacci sequence
"""

"""
1, 1, 2, 3, 5, 8, 13, 21, 34, ......
"""


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n < 1:
        return "error"
    else:
        return fibonacci(n-1) + fibonacci((n-2))


print("Tips: If you enter a number greater than or equal to 35, you may need to wait for a while")

n = input("Please enter one number to calculate the n th item of a Fibonacci sequence: ")
n = int(n)

print(fibonacci(n))



# test
print("\n")
print("[info]starting test...")
for i in range(1, 100):
    print(fibonacci(i), end="\n")
print()
print("[info]test end.")



