"""
2.Python Program to Display the multiplication Table

print out a multiplication table
12X1  12X2  12X3 ... 12X12

12x1 = 12
12x2 = 24
12x3 = 36
...
12x12 = 144

using for-loop and string format
"""

# Neison
for i in range(1, 13):
    print("12 x", i, "=", 12 * i)

# Max
for i in range(13):
    print("12x{} = {}".format(i, i * 12))

# Ken
second_number = list(range(1,13))
for the_second_number in second_number:
    print("12 *", the_second_number, "= {}".format(12*the_second_number))

# Kevin
for i in range(1, 13):
    product = 12 * i
    print("12 X {:2} = {:3}".format(i, product))

# Yixuan
for i in range(1, 13):
    print("12 x {} = {}".format(i, 12 * i))



"""
v2. if you input a number A
print out a multiplication table
A X 1 = A
A X 2 = ..
A X 3 = ..
....
A X A = ...

"""

# Steven
num = int(input("Steven: Enter a number:"))
for i in range(1, num + 1):
    print("{} x {} = {}".format(num, i, num * i))

# v2 - kevin
number = input("Kevin:Please enter one number : ")
number = int(number)
for i in range(1, number + 1):
    product = number * i
    print("{} X {:2} = {:3}".format(number, i, product))

# Yixuan
a = int(input("Yixuan: Please enter a number: "))
for i in range(1, a + 1):
    print("{} x {} = {}".format(a, i, a * i))


# Neilson
num = int(input("Neilson: Please enter a number: "))
for i in range(1, num + 1):
    print("{} x {} = {}".format(num, i, num * i))

# Max
A = int(input("Max: Input a number: "))
for i in range(1, A + 1):
    print("{}x{} = {}".format(A,i,i * A))






