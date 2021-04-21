"""
yield
"""



def f1():

    num = 0
    while True:
        num += 1

        if num >10 :
            break

        yield num

    # return a,b,c

# main
print(list(f1()))