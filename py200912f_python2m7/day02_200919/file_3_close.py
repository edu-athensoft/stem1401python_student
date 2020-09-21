"""
closing
close()
"""

f3 = None
try:
    f3 = open('file3.txt')
    print(f3)

except FileNotFoundError as e:
    print("No such file.")

except Exception as e:
    print("Unknown error.")

finally:
    f3.close()
    print("f3 closed.")

"""
1. Write a Python program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
e.g. User inputs 5
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

2. Write a program to sort a dictionary by key in both ascending and descending order.

3. Write a program to sort a dictionary by value in both ascending and descending order.

"""