"""
recursive function

fact: a function can call another function in itself

"""



def foo2():
    global counter
    print("foo2() for ", counter)
    counter += 1
    foo2()

counter = 1

foo2()
