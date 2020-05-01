"""
recursive function

fact: a function can call itself

"""

# 1+2+3+4+5+6+....+100   = 5050

# y = f(x)

"""
s(1) = 1
s(2) = (1) + 2      = s(1) + 2
s(3) = (1+2) + 3    = s(2) + 3
s(4) = (1+2+3) + 4  = s(3) + 4
...
s(n) = (1+2+...+ (n-1)) +n = s(n-1) +n

s(n) = n + s(n-1)   case 2:  n>1

-----------
s(100) = s(99)+ 100
s(99) = s(98) + 99
...
s(2) = s(1) +2
s(1) = 1            case 1:  n=1

                    case 3:  n<1

"""


def sum(n):
    if n == 1:
        return 1
    elif n >1:
        return n+ sum(n-1)
    else:
        print("invalid number")

result = sum(100)
print(result)


# homework
# calculate the factorial of n (n>0, n is an Integer)
# 1X2X3X4......xn
# p(100)  = 100x99x98x97x...x1
# p(6)  = 6x5x4x3x2x1