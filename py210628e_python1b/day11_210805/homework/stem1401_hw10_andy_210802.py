"""
[Homework]
Date: 2021-08-02
Quiz 10
file name pattern: stem1401_hw10_andy_21mmdd.py
Due date: 2021-08-04
"""

"""
q1:
                       <-------------------------^
                       |                         |
                       V                         |
start -> has loop reached last item? -> true -> print
                                     -> false -> stop loop
"""

# q2:
product = 1

N = 20

START = 2
STOP = N + 1
INTERVAL = 2

for i in range(START, STOP, INTERVAL):
    product = product * i
print(product)

print('===========================')

# q3:
average = 0
score = [85, 78, 96, 85, 73, 59, 45]
num_people = len(score)

for num in score:
    average = average + num / num_people

A_num = 0

if score[0] > 90:
    A_num += 1
if score[1] > 90:
    A_num += 1
if score[2] > 90:
    A_num += 1
if score[3] > 90:
    A_num += 1
if score[4] > 90:
    A_num += 1
if score[5] > 90:
    A_num += 1
if score[6] > 90:
    A_num += 1

print('The average score in this class is {}, and {} student/students got A.'.format(average, A_num))

print('===========================')
