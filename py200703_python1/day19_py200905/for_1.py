"""
loop

1. for-loop
2. while-loop

iteration
iterating
iterable (adj. n.)
traversal

"""

# case 1. print out N for given times

N = 10
# print(N)
# print(N)
# print(N)
# print(N)
# print(N)
# print(N)
# print(N)
# print(N)
# print(N)
# print(N)

# counts = [0,1,2,3,4,5,6,7,8,9]
# case 1.
counts = [1,2,3,4,5,6,7,8,9,10]
for x in counts:
    print(N)
    print(N, x)
print()

# case 2. list
friends = ['Peter','Amy','Andy','Tom','Jack']
print(friends)

for name in friends:
    print(name)
print()

# case 3. tuple
day_of_week = ('MON','TUE','WED','THU','FRI','SAT','SUN')
for day in day_of_week:
    print(day)
print()

# case 4. string
word = 'Python'
for char in word:
    print(char)