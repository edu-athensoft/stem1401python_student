"""
Fibonacci sequence:
ib2, ib1, 1, 1,	2,	3,	5,	8,	13,	21,	34,	55, ...


set up: ib2=1, ib2=0
why?
(1, 0,, 1, 1, 2, 3, ...) correct
(0, 1,, 1, 1, 2, 3, ...) incorrect

"""
def fibo(pos):
    ib2 = 1
    ib1 = 0
    item = 0
    for pos in range(pos):
        item = ib1 + ib2
        ib2 = ib1
        ib1 = item
    return item

for x in range(1,11):
    print(fibo(x), end="\t")