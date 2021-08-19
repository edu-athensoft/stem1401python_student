"""
write a python program to check prime number

An integer p can only be perfectly divided by 1 and itself, then p is a prime number
"""

num = int(input('enter an integer:'))


start = 2
# stop = num - 1

for i in range(start, num):
    # print(i)
    if num % i == 0:
        print('{} is not a prime number'.format(num))
        print(i)
        break
        # continue
else:
    print('{} is a prime number'.format(num))
