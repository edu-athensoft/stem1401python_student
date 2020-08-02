"""
numbers - decimal

Due to this reason, most of the decimal fractions cannot be accurately stored in our computer.

"""

a = 1.1 + 2.2
# print(a)

b = 3.3
# print(b)

if a == b:
    print("a==b")
else:
    print("a!=b")


a = 1.1 + 0.1
b = 1.3 - 0.1
if a == b:
    print("a==b")
else:
    print("a!=b")

print()

# question
# 1.1 + 2.2 == 3.3

print(1.1 + 2.2 == 3.3)
print(float(1.1)+float(2.2)==float(3.3))
print()

print(1.1)
print(2.2)
print(3.3)
print(1.1+2.2)
print()


print(1.1+2.2 > 3.3)
print(1.1 + 2.2 == 3.3)
print(1.1+2.2 < 3.3)
print()


# other example
print("=== example 2 ===")
f11 = 1.0
f12 = 0.1
f2 = 0.9
print("f11={}, f12={} and f2={}".format(f11,f12,f2))
print("{}-{} == {} ?".format(f11, f12, (f11-f12 == f2)))
print("f11-f12 > f2 ?",f11-f12 > f2)
print("f11-f12 < f2 ?",f11-f12 < f2)
print()


# decimal
print("=== example 3 ===")
f11 = 1.0
f12 = 0.3
f2 = 0.7
print("f11={}, f12={} and f2={}".format(f11,f12,f2))
print("f11-f12 == f2 ?",f11-f12 == f2)
print("f11-f12 > f2 ?",f11-f12 > f2)
print("f11-f12 < f2 ?",f11-f12 < f2)
print()

# faction
print("=== example 4 ===")
f11 = 1.0
f12 = 0.33
f2 = 0.67
print("f11={}, f12={} and f2={}".format(f11,f12,f2))
print("f11-f12 == f2 ?",f11-f12 == f2)
print("f11-f12 > f2 ?",f11-f12 > f2)
print("f11-f12 < f2 ?",f11-f12 < f2)
print()

print(1.0-0.33)



