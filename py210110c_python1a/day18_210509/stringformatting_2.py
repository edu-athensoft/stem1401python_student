"""
string formatting
"""

result = 'Hello {}, your balance if {}'.format('Adam', 230.235)
print(result)

result = 'Hello {0}, your balance if {1:9.3f}'.format('Adam', 230.235)
print(result)

result = 'Hello {0}, your balance if {1:9.2f}'.format('Adam', 230.232)
print(result)

# question:
# Was it truncated or rounded?