"""
stem1402_python_homework_4_steven
"""

# 1. Calculate the n item of a Fibonacci sequence

def fibonacci(n):
    if n < 0:
        print("Error")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

print(f"The 10 item from the Fibonacci sequence is {fibonacci(10)}")

