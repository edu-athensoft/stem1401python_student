# flow control - if statement

level = int(input("Enter your current level: "))

# 0 - 19.99,  20 - 49.99,   50 +

if level>=50 :
    print("buy my sword of lvl 50")
    print("collecting mineral")
elif level>=20 :
    print("buy a stick of lvl 20")
    print("farming")
else:
    print("My current level is {}".format(level))
    print("farming")

