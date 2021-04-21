"""

else clause

try:
    pass
except:
    pass
else:
    pass

keyword:
assert
is to predict there would be an error if the expr returns false.

raise
"""

# program to print the reciprocal of even numbers

print("Reciprocal Program")

try:
    num = int(input('Enter a number: '))

    assert num % 2 == 0

except AssertionError as ae:
    print(ae)
    print("Not an even number")

else:
    reciprocal = 1/num
    print(f'reciprocal = {reciprocal}')


print("end")