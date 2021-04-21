"""
recursive function

product of number sequence

1x2x3x4x5x6....x10

factorial
f(n)
n!

f(n)    = n * f(n-1)
f(n-1)  = (n-1) * f(n-2)
...
f(2) = 2 * f(1)
f(1) = 1

"""


def f(n):
    if n == 1:
        return 1
    return f(n-1) * n


result = f(10)
print(f"The prod is {result}")




numbers = [1,2,3,4,5,6,7,8,9,10]

print("=== start ===")

prod = 1
for n in numbers:
    prod *= n
print(f"The product is {prod}")

print("=== end ===")


