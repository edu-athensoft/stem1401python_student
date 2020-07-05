"""
Quiz 8
"""

# 8.
sentence = input("Enter a sentence:")
if "A" in sentence or "a" in sentence:
    print("There is an A")
else:
    print("There is no A")

# 9.
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

print(list1 == list2)
print(list1 is list2)

# 10.
# If it is May 22
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
day2 = days.index('Fri')
future = (day2 + 100) % 7
if int(future) == 0:
    print(days[0])

elif int(future) == 1:
    print(days[1])

elif future == 2:
    print(days[2])

elif future == 3:
    print(days[3])

elif future == 4:
    print(days[4])

elif future == 5:
    print(days[5])

else:
    print(days[6])
