# python function

def get_sum():
    '''1+...+10'''
    sum = 0
    for i in range(1, 11):
        sum = sum + i

    print(sum)


get_sum()