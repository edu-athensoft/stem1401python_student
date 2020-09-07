"""
for loop

Get the sum of a number sequence
1 + 2 + 3 + 4 + 5 + .... + 100 = 5050

from 1 to 10 = 55

"""

"""
analysis 

1. how to represent the data
2. for loop, determine the number of iteration
   10 times
3. how to do addition

sum = 0

NO.  n        
----------------
#01. 1 + 0 -> 1
#02. 2 + 1 -> 3
#03. 3 + 3 -> 6
#04. 4 + 6 -> 10
#05. 5 + 10 -> 15
#06. 6 + 15 -> 21
#07. 7 + 21 -> 28
#08. 8 + 28 -> 36
#09. 9 + 36 -> 45
#10. 10+ 45 -> 55

sum = n + sum

"""

numbers = [11,22,32,42,52,61,72,81,92,101]

# len(numbers)

sum = 0
for n in numbers:
    # print(n)
    sum = n + sum
    # print(n, sum)

print("The sum of the sequence is {}".format(sum))







