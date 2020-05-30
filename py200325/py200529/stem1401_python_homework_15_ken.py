"""
For May 29th, 2020.
stem1401_python_homework_15_ken
Quiz 10.
"""

# Question 2.
product = 1
for number in range(2,21,2):
    product *=number
    print(number)
print(product)


# Question 3

average_score = 0
total = 0
nb_A_students = 0

student_score_list = (
    ("Marie", 85),
    ("Phoebe", 78),
    ("Sabrina", 96),
    ("Emma", 85),
    ("Amy", 73),
    ("Isabelle", 59),
    ("Clark", 45),
)

for student_score in student_score_list:
    total += student_score[1]
    print(total, "total")
    if student_score[1] >= 90:
        nb_A_students += 1

average_score = total/len(student_score_list)
print("The average is around {:.2f} and {} student(s) got A.".format(average_score, nb_A_students))


# Question 4 : 9x9 multiplication table

row = 1


for second_factor in range(1, 10):
# Each row's first factor ranges from 1 to the second factor (that's why for each row it's range(1, second_factor + 1)
    for first_factor in range(1, second_factor + 1):
        # Row changes when the second factor changes
        if second_factor != row:
            print("\n")
        row = second_factor
        # Two formats:
            # First format: Put numbers.
            # Second format: Put same string length (9).
        without_format_align = "{}*{}={}".format(first_factor, second_factor, first_factor * second_factor)
        with_format_align = "{:<9}".format(without_format_align)
        print(with_format_align, end="")
