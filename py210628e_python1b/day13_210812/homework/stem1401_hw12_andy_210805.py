"""
[Homework]
Date: 2021-08-05
Quiz 11
Due date: this Wednesday
"""

"""
q1:
pseudo-code
start -> A -> True -> B -> back to A
           -> False -> end
"""

# q2:
num_terms = int(input("How many terms?(integer number only) : "))

num_1 = 0
num_2 = 1
count = 0

if num_terms <= 0:
    print("Error, this is not a positive integer! Please try again.")

else:
    print("Fibonacci sequence:")
    while count < num_terms:
        print(num_1)
        nth = num_1 + num_2
        num_1 = num_2
        num_2 = nth
        count += 1
print('end')
