"""
Quiz 10
"""
# Question 2
one = 1

for i in range(2, 20, 2):
    one *= i
print("1 x 2 x 4 ... x 20 = {}".format(one))


# Question 3

Kids = ["Marie", "Phoebe", "Sabrina", "Emma", "Amy", "Isabelle", "Clark"]
Kids_score = {
    "Marie": 85,
    "Phoebe": 78,
    "Sabrina": 96,
    "Emma": 85,
    "Amy": 73,
    "Isabelle": 59,
    "Clark": 45
}

Sum = 0
count = 0


for i in Kids:
    Sum += Kids_score[i]
    if Kids_score[i] >= 90:
        count += 1

Average = Sum / len(Kids)
print("The average of the class is {:.2f} and the number of students who got an A is {}.".format(Average, count))