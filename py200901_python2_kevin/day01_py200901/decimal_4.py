"""
decimal

getcontext()

"""

print(16.0/7)
# get the length of the result
print(len(str(16.0/7))-2)


from decimal import getcontext, Decimal

# Set the precision.
getcontext().prec = 3

output = Decimal(16.0)/Decimal(7)

print(output)



# the get the list of attributes or definitions in a module
import decimal
# print(dir(decimal))

for i in dir(decimal):
    print(i)


