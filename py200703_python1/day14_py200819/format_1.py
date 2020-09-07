"""
for positional argument
for keyword argument
"""

s = "Hello {}, your balance is {}".format("Adam",230.2346)
print(s)

s = "Hello {0}, your balance is {1:9.3f}".format("Adam",230.2346)
print(s)

s = "Hello {0}, your balance is {1:12.2f}".format("Adam",230.2346)
print(s)

s = "Hello {0}, your balance is {1:12.1f}".format("Adam",230.2346)
print(s)


s = "Hello {0}, your balance is {1:12.3f}".format("Adam",230.2346)
print(s)


s = "Hello {name}, your balance is {blc:12.3f}".format(name="Adam",blc=230.2346)
print(s)

print()
s = "Hello {}, your balance is {}".format("Bill Gates",12300.2346)
print(s)

