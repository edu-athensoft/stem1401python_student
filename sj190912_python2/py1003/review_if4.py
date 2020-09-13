# flow control - if statement

# 0 - 9.99 buy a knife
# 10 - 19.99 buy a armor
# 20 - 29.99 buy a pair shoes
# 30 - 39.99 buy a pendent
# 40 - 49.99 buy an earing
# 50 - 50.99 buy a ring
# 60 - 69.99 buy a sword
# 70 arena
while(True):
    level = int(input("Enter your current level: "))

    if level < 0:
        print("Your level is invalid.")
        break;

    if level <10:
        print("buy a knife")
    elif level < 20:
        print("buy an armor")
    elif level < 30:
        print("buy a pair shoes")
    elif level < 40:
        print("buy a pendent")
    elif level < 50:
        print("buy an earing")
    elif level < 60:
        print("buy a ring")
    elif level < 70:
        print("buy a sword")
    else:
        print("can go to arena")



print("bye-bye")





