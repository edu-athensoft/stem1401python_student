"""
while with condition at the top, in the middle, at the bottom
"""

# sample 1.
sum = 0
i = 1

n = 10

while i < n:
    sum += i
    i += 1

# print("The sum is {}".format(sum))


# sample 2.
# vowels = 'aeiouAEIOU'
#
# while True:
#     v = input("Enter a vowel")
#     if v in vowels:
#         break
#     print("That is not a vowel. Try again")
#
# print("Thank you")


# sample 3.
while True:
    a = input("Enter a number")
    print(a)
    if a == '0':
        break