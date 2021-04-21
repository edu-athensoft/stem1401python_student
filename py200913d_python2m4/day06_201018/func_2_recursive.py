"""
recursive function

summary of number sequence

s(n) = s(n-1) + n

s(10) = s(9) + 10
s(9) = s(8) + 9
...
s(1) = 1

"""


def s(n):
    if n == 1:
        return 1
    return s(n-1) + n


result = s(10)
print(f"The sum is {result}")



"""
numbers = [1,2,3,4,5,6,7,8,9,10]

print("=== start ===")

sum = 0
for n in numbers:
    sum += n
print(f"The sum is {sum}")

print("=== end ===")
"""

