"""
simulate do-while loop with python
"""

# while True:
#     print("this is a while loop")
#     if 5 >3 :
#         break


# input a number
# if this number does not fall in [1-10]
# re-enter

num = int(input("Enter a nunber [1-10]: "))

while num <1 or num > 10:
    num = int(input("Enter a nunber [1-10]: "))

print("The number you input is {}".format(num))



