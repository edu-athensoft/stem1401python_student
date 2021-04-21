"""
mini calculator


user can input option (adding, subtracting, mul, div, //, %, **)
to perform arithmetic operation

user can input option (logical and, or, not)
to perform logical operation

after user selected one option of operation, he/she is asked to input operand(s)

The system print out the result with necessary message(prompt)

"""

"""
Hint:
1. one task one function, one function per task
2. consider how to  input info for option and operand
3. consider how to output properly

code quality
4. consider the program structure
5. comment
6. naming convention
"""

"""
plan
1. input
2. how to select an option(add,sub,mul or div)
3.

"""

def addition(x,y):
    x + y

def subtraction(x,y):
    x - y

def multiplication(x,y):
    x * y

def division(x,y):
    x / y

print("=== Mini calculator ===")
print("Please select an option")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1':
            print(x, "+", y, "=", addition(x , y))

        elif choice == '2':
            print(x, "-", y, "=", subtraction(x , y))

        elif choice == '3':
            print(x, "*", y, "=", multiplication(x , y))

        elif choice == '4':
            print(x, "/", y, "=", division(x , y))
            break
    else:
        print("Invalid")
