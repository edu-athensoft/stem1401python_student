"""
1. get values from a dictionary and remove duplicated values
print out the result of value

"""

mydict = {'s001': 97,
          's002': 94,
          's003': 87,
          's004': 90,
          's005': 94}

# step 1. get values
result = list(mydict.values())
print(result)

# step 2. remove if applicable
# t1 = (1,1,1,2,2,2)
# print(t1)

# list -> set
result2 = set(result)
print(result2)

