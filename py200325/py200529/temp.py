for i in range(1,10):
    for x in range(1,i+1):
        print("{}*{}={}".format(x,i,x*i), end="\t")
    print()


# Question 2.
# product = 1
# for number in range(2,21,2):
#     product *=number
#     print(number)
# print(product)


# Question 3

# average_score = 0
# total = 0
# nb_A_students = 0
#
# student_score_list = (
#     ("Marie", 85),
#     ("Phoebe", 78),
#     ("Sabrina", 96),
#     ("Emma", 85),
#     ("Amy", 73),
#     ("Isabelle", 59),
#     ("Clark", 45),
# )
#
# for student_score in student_score_list:
#     total += student_score[1]
#     print(total, "total")
#     if student_score[1] >= 90:
#         nb_A_students += 1
#
# average_score = total/len(student_score_list)
# print("The average is around {:.2f} and {} student(s) got A.".format(average_score, nb_A_students))

"""

# Question 3. A class of student just look a midterm exam on French course.
# Please figure out the average of this class. And how many students got A.

# s is score, and s is student
s_s = [
    ("Marie", 85),
    ("Phoebe", 78),
    ("Sabrina", 96),
    ("Emma", 85),
    ("Amy", 73),
    ("Isabelle", 59),
    ("Clark", 45),
]

# name = ["Marie", "Phoebe", "Sabrina", "Emma", "Amy", "Isabelle", "Clark"]
# score = [85, 78, 96, 85, 73, 59, 45]

score_total = s_s[0][1] + s_s[1][1] + s_s[2][1] + s_s[3][1] + s_s[4][1] + s_s[5][1] + s_s[6][1]
average_score = score_total / len(s_s)

# print(score_total)
print("The average score is {:.2f}".format(average_score))

# how many people get A
number = 0
for score in s_s:
    if score[1] >= 90:
        number = number + 1

print("{} students got an A.".format(number))
"""