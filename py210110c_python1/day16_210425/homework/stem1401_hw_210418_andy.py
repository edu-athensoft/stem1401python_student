"""
[Homework]
Date: 2021-04-18
Quiz 6   q1-q6
Due date: by the end of next Sat.
"""


"""
q1:
standard input device:
keyboard

standard output device:
screen

q2:
input device:
mouse, webcam

output device:
Printer, stereo
"""

# q3
print('question 3 start here')
input()
print('===done===')

# q4
print('question 4 start here')
print(input('Please write down your username:'))
print('===done===')

# q5
# answer 1: It depends on how many input codes the programmer has entered
# answer 2: <class 'builtin_function_or_method'>
print('question 5 start here')
a = type(input)
print('The datatype of a raw input =', a)
print('===done===')


# q6
print('question 6 start here')
print("=== Google login form ===")
username = input('Please enter your username:')
password = input('Please enter your password:')
print()

print("Welcome back", username, "!")
print("Username:", username)
print("Password:", password)
print("You can save your password in Google and next it will automatically login for you!")
print('===done===')
