"""
project: Input a valid number
user is asked to input a number [1-10]
if the user failed to input a valid number,
he/she will be asked to input again until he/she input a valid number
"""

# kevin
numbers = [1,2,3,4,5,6,7,8,9,10]

num = int(input("Please enter a number from 1 - 10: "))

while num not in numbers:
    num = int(input("Please enter a number from 1 - 10: "))

