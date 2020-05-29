"""
while loop
"""

greetings = "Hello world!"

# method 1
counter = 10

while counter > 0:
    print(greetings, counter)
    counter = counter - 1

print("the lastest counter is {}".format(counter))


# method 2
# counter = 0
counter = 1

while counter <= 10:
# while counter < 10:
    print(greetings, counter)
    counter = counter + 1

print("the lastest counter is {}".format(counter))
