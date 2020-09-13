import random

#
print("aaa")
print("bbb")
print("ccc")



for x in range(0,10):
    a = random.randint(1,6)
    print(a, end=",")
    if (x+1)%2==0 :
        print()
