"""
string formatting

for keyword argument
positional argument => keyword(named) argument
"""

result = 'Hello {}, your balance if {}'.format('Adam', 230.235)
print(result)

result = 'Hello {0}, your balance if {1:9.3f}'.format('Adam', 230.235)
print(result)

result = 'Hello {0}, your balance if {1:9.2f}'.format('Adam', 230.232)
print(result)

result = 'Hello {0}, your balance if {1:9.0f}'.format('Adam', 230.832)
print(result)

# question:
# Was it truncated or rounded?
# Andy
result = 'Hello {name}, your balance is {balance:9.2f}'.format(name='Andy', balance=123.456)
print(result)

# Leonj
result = 'hello {my_name}, your balance is {mybalance:9.2f}'.format(my_name='adam', mybalance=230.235)
print(result)

# Yiding
result = 'Hello {name}, your balance is {balance:9.2f}'.format(name='Yiding', balance=230.235)
print(result)


