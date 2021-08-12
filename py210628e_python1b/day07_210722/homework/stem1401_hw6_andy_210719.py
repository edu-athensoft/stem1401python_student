"""
[Homework]
Quiz 8
Due date : 2021-07-21
Andy
"""


"""
q1:
+, -, *, /, //, %, **

q2:
>, >=, <, <=, ==, !=

q3:
and, or, not

q5:
is, is not

q6:
in, not in

q7:
'x += 1' = 'x = x + 1'
"""

# q8: ?
a = True
A = True
character = a
if character == a and character == A:
    print('True')
else:
    print('False')
# not done(don't know how to do)


# 8. solution
sentence = 'This is my favorite game.'
# if 'a' in sentence:
#     print("The sentence contains a.")
#     # print(True)
# if 'A' in  sentence:
#     print("The sentence contains A.")

if 'a' in sentence or 'A' in sentence:
    print("The sentence contains \'a\' or \'A\'.")




# q9:
list1 = [1,2,3]
list2 = [1,2,3]
if list1 == list2:
    print('same')
else:
    print('not same')

# q10:
today = 5
a = 100 // 7
b = 100 - 7 * a
c = today + b
if c <= 7:
    print(c)
else:
    print(c-7)


today = 1
total_days = 300
answer_day = (total_days % 7 + today)%7
# print(answer_day)


if answer_day == 1:
    answer_day = "Mon"
if answer_day == 2:
    answer_day ="Tue"
if answer_day == 3:
    answer_day ="Wed"
if answer_day == 4:
    answer_day ="Thu"
if answer_day == 5:
    answer_day ="Fri"
if answer_day == 6:
    answer_day ="Sat"
if answer_day == 0:
    answer_day ="Sun"

print('{} days later, it would be {}'.format(total_days,answer_day))

