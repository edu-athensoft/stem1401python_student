"""
if statement

story:

What will we do for today?

if it is sunny , we then hang out for shopping.

if it is rainy, we then stay home and play video game.

please write some code to describe the decision making statement above.
"""



# find out or determine the condition

# case 1.
is_sunny = True
# is_sunny = False

if is_sunny :
    print("hang out for shopping")


# case 2.
is_rainy = False

if is_rainy:
    print('stay home and play video game')



# Summary
# is_xxxx = True | False
# if is followed by
# boolean value (aka boolean literal)
# boolean variable/constant,
# comparison expression,
# logical expression
# mixture of above  (logical expression)

is_a = True
is_b = False

expr = is_a and is_b or 5>3 and True

print("=============================")

# example 2.
# 0: sunny
# 1: cloudy
# 2: snowy
# 3: rainy
weather = 2

if weather==1:
    print("hang out for shopping")

if weather==0:
    print('stay home and play video game')

if weather <= 1:
    print('stay home and eat food')







