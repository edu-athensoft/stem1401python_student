"""
[Challenge] Find the max number

assuming max number comes from a number sequence

1. fixed number sequence
2. input from keyboard
3. import from other data files or database
4. transfer from other program or result

choose an easy way to generate the num. seq.

decision:
1. fixed number sequence
2. what data type? how many variables or constants?
3. can I use loop?
   repeatable work pattern? formula?
   start number=?
   stop number=?
   index?
4. what is the algorithms?
   compare with max number one by one
   scan all number in a particular order

    i.e. 1,2,3,4,5,6,7,8,9

5. what if when the input data (aka num. seq.) changes, this program can still work properly?

"""


# data
numlist = [2,3,5,6,4,7,8,5,2,3,4,2,9,2,3,5,6,4,7,8,5,2,3,4,2,1]
LENGTH = len(numlist)

# for index in range(LENGTH):
#     print("numlist[{}] is {}".format(index, numlist[index]))

# get the max number
max = numlist[0]
for index in range(LENGTH):
    current_num = numlist[index]
    print("numlist[{}] is {}".format(index, current_num))

    if current_num>max:
        max = current_num


# output the result
print("The max number of the sequence: {} is {}".format(numlist, max))








