"""
output

print()

Syntax
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

"""


# print(*args) - print out multiple values
# print()

# pass in one argument
print(1)

# pass in two arguments, using comma as separator
print('abc','xyz')

# pass in more than two args.
print(1,2,3,5,67,7,8)


# print(sep=' ')   default value of sep is ' '
# sep stands for separator
# print(1,2,3,4,5, sep='&')
print(1,2,3,4,5, sep=',')
print(1,2,3,4,5, sep=', ')
print(1,2,3,4,5, sep=',  ')

# named parameters must stay after the ones without name
# print(sep=',  ', 1,2,3,4,5 )
# print(1,2,3,sep=',  ', 4,5 )

# default value of sep is ' ', in that case you can omit the sep
print('abc')
print('abc',sep=' ')


# end='\n' in default
print("=== end option ===")
print(1,2,3)
print(4,5,6)
print(1,2,3,4, end="&&&")
print(1,2,3,4, end="&&&\n")
print("=== end of end option ===")




# ex. print out your subjects one by one using a given separator ';'
#
subjects = ['math','history','French','art','science']
# sep=';'
# print(subjects)

# write your code using only one print statement
# how to access items from a list
# [] index


# Andy 2
# subjects = ['math', 'history', 'french', 'art']
# print('The #0 item of list is', subjects[0])
# print('The #1 item of list is', subjects[1])
# print('The #2 item of list is', subjects[2])
# print('The #3 item of list is', subjects[3])
# print(subjects[0], subjects[1], subjects[2], subjects[3], sep=';')

subjects = ['math', 'history', 'french', 'art']
print(subjects[0], subjects[1], subjects[2], subjects[3], sep=';')


# Kevin 1
print(subjects, sep=';')
subjects = ['math', 'science', 'history', 'french', 'art']
print(subjects[0], subjects[1], subjects[2], subjects[3], sep=';')


# Leon
animals = ['horse', 'dog', 'cat', 'mouse']
print(animals[0], animals[1], animals[2], animals[3], sep=';')


# Yiding
sports = ['basketball', 'soccer', 'tennis', 'baseball']
print(sports[0], sports[1], sports[2], sports[3], sep=';')



# ex. print out a matrix (2D Array)
# row = 2, column = 2
# M2x2

# M3X4

# M4X3

matrix = [[1,2],
         [3,4]]
print(matrix)

print(matrix[0][0])
print(matrix[0][1])
print(matrix[1][0])
print(matrix[1][1])

print("=== matrix ===")
print(matrix[0][0], matrix[0][1])
print(matrix[1][0], matrix[1][1])
print("=== matrix ===")

print(matrix[0][0], matrix[0][1], '\n', matrix[1][0], matrix[1][1])















