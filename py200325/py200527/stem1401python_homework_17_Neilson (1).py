"""
Quiz 9
"""

# Question 1

# case 1. if

if 5 > 2:
    print("hello")

# case 2. if-else

if 5 < 2 == True:
    print("hello")
else:
    print("bye")

# case 3. if-elif-else

num = 10

if num > 10:
    print("{} is greater than 10".format(num))
elif num == 10:
    print("{} equals 10".format(num))
else:
    print("{} is smaller than 10".format(num))

# case 4. nested if
if num > 5:
    if num > 15:
        print("{} is greater than 10".format(num))
    else:
        print("{} is smaller than 15".format(num))
else:
    print("{} is smaller than 5".format(num))

# Question 2

numbers_list = [3, 2, 5, 6, 4, 7, 9, 1, 10, 8]

biggest_number = numbers_list[0]
smallest_number = numbers_list[0]

for numbers in numbers_list:
    if biggest_number < numbers:
        biggest_number = numbers
    if smallest_number > numbers:
        smallest_number = numbers

print("The biggest number is {b} and the smallest number is {s}.".format(b=biggest_number, s=smallest_number))

# Extra Question

product_of_numbers = 1
for num in range(1, 101):
    product_of_numbers = product_of_numbers * num

print("The product of the numbers 1 to 100 is {}.".format(product_of_numbers))