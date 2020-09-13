import math

# mylist1 = [30,40,49,52,78,100]
# a = list(map(lambda x : math.sqrt(x) * 10, mylist1))
# print(a)

mylist1 = [30,40,49,52,78,100]
a = list(map(lambda x : round(math.sqrt(x) * 10) ,mylist1))
print(a)


print(round(54.772255750516614))
print(round(63.24555320336759))
print(round(70.0))
print(round(72.11102550927978))
print(round(88.31760866327848))
print(round(100.0))
