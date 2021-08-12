"""
q3
"""

total_score = 0
average = 0
a_num = 0
scores = [85, 78, 96, 85, 73, 59, 45, 97, 89, 90]
num_people = len(scores)


for num in scores:
    total_score = total_score + num
    if num >= 90:
        a_num += 1

average = total_score / num_people

print("Average score is {:.1f}".format(average))
print("{} students of {} students got A.".format(a_num,num_people))