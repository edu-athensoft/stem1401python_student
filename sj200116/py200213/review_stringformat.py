"""
String format()
"""

# string template - string
# identifier
# reserved words
a = 1
b = 2
summary = a + b
print("{} + {} = {}".format(a, b, summary))

a = 10
b = 20
summary = a + b
print("{} + {} = {}".format(a, b, summary))

# ================
print("{1} + {0} = {2}".format(a, b, summary))

# ================
print("Hello {0}, your balance is {1:9.3f}".format("Adam",230.2346))

# ================
print("Hello {name}, your balance is {blc:9.3f}".format(name="Adam",blc=230.2346))

# =========
num = 10
print("This is a binary number: {}".format(10))
print("This is a binary number: {:d}".format(10))
print("This is a binary number: {:b}".format(10))
print("This is a binary number: {:x}".format(10))
print("This is a binary number: {:X}".format(10))
print("This is a binary number: {:%}".format(10))
print("This is a binary number: {:e}".format(10))
"""
decimal   binary    hexadecimal(16)
0              0        0
1              1        1
2             10        2
3             11        3
4            100        4
5            101        5
6            110        6 
7            111        7
8           1000        8
9           1001        9
10          1010        A
11          1011        B
12          1100        C
13          1101        D
14          1110        E
15          1111        F
16         10000       10
"""

"""
0-9         
"""
