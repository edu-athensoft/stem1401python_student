"""
for loop

Get the prod of a number sequence
1 x 2 x 3 x 4 x 5 x 6 x 7 x 8x 9x10 = ?

"""

"""
analysis 

1. how to represent the data
2. for loop, determine the number of iteration
   10 times
3. how to do factorial or multiplication


"""

numbers = [1,2,3,4,5,6,7,8,9,10]

# len(numbers)

prod = 1
for n in numbers:
    # print(n)
    prod = n * prod
    # print(n, sum)

print("The prod of the sequence is {}".format(prod))







