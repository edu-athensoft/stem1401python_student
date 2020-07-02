"""
stem1402_python_homework_3_steven
"""


# 1. Write a Python function to calculate the factorial of a number (a non-negative integer)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial1 = 1
        while n > 1:
            factorial1 *= n
            n -= 1
        return factorial1


num1 = int(input("Please enter a number to find its factorial:"))
print("Factorial of", num1, "is",
      factorial(num1))
print("------------------------------------------------------------------")
print()


# 2. Write a Python function to check whether a number is in a given range.

num1 = int(input("Please enter a number for checking:"))
print()
x = int(input("Please enter the first number of the range:"))
y = int(input("Please enter the second number of the range:"))
print()


def range_test(num1):
    if num1 in range(x,y):
        print(num1, "is in range.")
    else:
        print(num1," is not in range.")


range_test(num1)
print("------------------------------------------------------------------")
print()


# 3. Write a Python function that calculates the number of upper case letters and lower case letters.

str1 = input("Please write a sentence:")
print()


def counter(string):
    lowercase = 0
    uppercase = 0
    for letter in str1:
        if letter >= "a" and letter <= "z":
            lowercase += 1
        if letter >= "A" and letter <= "Z":
            uppercase += 1

    print("There are {} uppercase letters in {}".format(uppercase, str1))
    print("There are {} lowercase letters in {}".format(lowercase, str1))


counter(str1)
print("------------------------------------------------------------------")
print()





