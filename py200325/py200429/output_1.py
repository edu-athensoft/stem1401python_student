"""
syntax
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

"""

# *object
print()
print(1)
print(1, 2)
print(1, 2, 'mystr')
print(1, 2, 'mystr',1, 2, 'mystr')

print("-------")

# sep=' '
print(1, 2, 'mystr',1, 2, 'mystr', sep=',,')

# end='\n'
print("-------")
print(1, end='\t')
print(2, end='\t')
print(3, end='\t')
print(4, end='\t')
print(5, end='\t')
print(6, end='\t')
print(7)
print("-------")

print("-------")
print(1, end='&&')
print(2, end='&&')
print(3, end='&&')
print(4, end='&&')
print(5, end='&&')
print(6, end='&&')
print(7)
print("-------")


"""
[Homework]
1. Research
What is an Array?
What is a Matrix?
Hints:
	Quotation or citation is required.
	Examples are mandatory.


2. Print out a matrix by 3x4
Hints:
3 rows by 4 columns
Choosing proper data type(s) for data
	Using print() and set proper arguments

Instruction:
	Please submit 2 files:
	One for the research
	One for the program

"""




