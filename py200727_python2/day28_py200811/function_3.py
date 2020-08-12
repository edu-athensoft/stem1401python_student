"""
arguments

return value|expression
"""


# case 2.
def add(num1, num2):
    # num1 = 1
    # num2 = 2

    res = num1 + num2
    return res
    # print(res)

result = add(3, 5)
# print(f"The result is {result}")
print("The result is {}".format(result))


# case 3. to return multiple values
def calc(num1, num2):
    sum = num1+num2
    prod = num1 * num2
    return sum, prod

mysum, myprod = calc(1,2)
print("The sum of {} and {} is {}".format(1,2, mysum))
print("The prod of {} and {} is {}".format(1,2, myprod))

