"""
ex 2.
write a program to find the smallest number among 3 given numbers
"""

numbers = [24, 115, 6, 78, 45, 23, 67]

max = numbers[0]

# 1st round
if max < numbers[0]:
    max = numbers[0]

# 2nd round
if max < numbers[1]:
    max = numbers[1]

# 3rd round
if max < numbers[2]:
    max = numbers[2]

# 4th round
if max < numbers[3]:
    max = numbers[3]

# 5th round
if max < numbers[4]:
    max = numbers[4]

# 6th round
if max < numbers[5]:
    max = numbers[5]

# 7th round
if max < numbers[6]:
    max = numbers[6]

print("The max number is {}".format(max))


