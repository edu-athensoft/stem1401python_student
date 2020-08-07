"""
python program to print all prime numbers in an interval

range (interval)
"""

# from 5 to 100, how many prime numbers are there in the list and what are they?


"""
i.e. (2..20)
expected result: 2, 3, 5, 7, 11, 13, 17,19
"""


#
# list1 = list(range(2, 21))
# a = range(2,21)
# print(a, type(a))

start = int(input("Enter the start number: "))
stop = int(input("Enter the stop number: "))

list1 = list(range(start, stop+1))
# print(list1)

for n in list1:
    # print(n)
    # if n is a prime number, then I print it out
    # otherwise I ignore it

    for i in range(2, n):
        if n % i == 0:
            # print("{} is not a prime number".format(num))
            # print(i, "times", num / i, "is", num)
            break
    else:
        print("{} is a prime number".format(n))



