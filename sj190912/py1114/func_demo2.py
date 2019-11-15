# python function

def get_sum(x):
    '''1+...+x'''
    sum = 0
    for i in range(1, x+1):
        sum = sum + i

    print("The summary of 1 to {} is {}".format(x,sum))


get_sum(10)
get_sum(5)
# print("The summary of 1 to {} is {}".format(10, a))