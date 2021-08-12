"""
expected result:
while loop 1
while loop 2
...
while loop 10

initial value of counter
boundary

"""

counter = 1

while counter < 11:
    print('while loop', counter)
    counter = counter + 1

print('end')



counter = 1

while counter <= 10:
    print('while loop', counter)
    counter = counter + 1

print('end')



counter = 0

while counter < 10:
    counter = counter + 1
    print('while loop', counter)


print('end')
