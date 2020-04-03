"""
comparing
"""


def compare(x, answer):
    flag = False
    if x > answer:
        print("Too big")
    elif x < answer:
        print("Too small")
    else:
        print("bingo")
        flag= True
    return flag


x = [50,70,20,60,69]
answer = 69

#
for i in range(5):
    isBingo = compare(x[i], answer)
    if isBingo:
        print("Congras!")
        break
    else:
        print("You have only {} chance(s) left! \n".format(5-i-1))
else:
    print("Please try another turn!")



