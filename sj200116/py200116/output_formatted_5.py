"""
positional arguments
"""

print("Hello {0}, your balance is {1:9.3f}".format("Adam",230.2346))
print("Hello {0}, your balance is {1:12.3f}".format("Adam",230.2346))
print("Hello {0}, your balance is {1:2.3f}".format("Adam",230.2346))


print("Hello {name}, your balance is {balance:9.3f}".format(name="Adam",balance=230.2346))
print("Hello {name}, your balance is {balance:9.2f}".format(name="Adam",balance=230.2346))
print()

print("Hello {name:9s}, your balance is {balance:9.2f}".format(name="Printer",balance=230.23))
print("Hello {name:9s}, your balance is {balance:9.2f}".format(name="USB",balance=10.26))
print("Hello {name:9s}z, your balance is {balance:9.2f}".format(name="HP Laptop",balance=1000.56))