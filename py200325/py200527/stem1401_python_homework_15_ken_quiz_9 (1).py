"""
For May 27th, 2020
Quiz 9.
"""

# Question 1

# 1. if

statement = "My house is here"
if "house" or "House" in statement:
    print("The statement contained the word house.")


# 2. if-else

age = 23
if age > 21:
    print("Welcome.")
else:
    print("You need to be older.")

# 3. if-elif...-else

nb_days = 30

if nb_days == 31:
    print("You are either in January, March, May, July, August, October or December.")
elif nb_days == 30:
    print("You are either in September, April, June or November")
else:
    print("You are in February.")



# 4. nested if

guessed_number = 15

if guessed_number < 10:
    print("The number is under 10.")
elif guessed_number < 20:
    print("The number is between 10 and 20.")
    if guessed_number % 5 == 0:
        print("The number is 15")
elif guessed_number < 30:
    print("The number is between 20 and 30.")
    if guessed_number % 5 == 0:
        print("The number is 25")
elif guessed_number < 40:
    if guessed_number % 5 == 0:
        print("The number is 35")
else:
    print("The number is over 40.")



# Question 2.

list_of_numbers = [2,4,5,-743,12,6,769,2134,32,-5]
biggest_number = list_of_numbers[0]
smallest_number = list_of_numbers[0]


for current_number in list_of_numbers:
    if current_number > biggest_number:
        biggest_number = current_number
    if current_number < smallest_number:
        smallest_number = current_number

print("The biggest number is {} and the smallest number is {}.".format(biggest_number,  smallest_number))



# Extra question.
all_product = 1
for i in range(1,101):
    all_product = i * all_product

print("The product of the numbers 1 to 100 is", all_product)