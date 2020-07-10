"""
stem1402_python_homework_4_p2_steven
"""

# 1.
def fib(nums):
    num1 = 0
    num2 = 1
    num3 = 0
    for nums in range(nums):
        num3 = num2
        num2 = num1
        num1 = num2 + num3
    return num1

nums = int(input("Please write the position of the fibonnaci number you want to check:"))

print(f"The {nums}th number from the fibonacci sequence is {fib(nums)}.")
