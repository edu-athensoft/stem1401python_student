"""
string1 = 'ab'
string2 = 'xy'

['ax','ay','bx','by']

"""

string1 = 'ab'
string2 = 'xy'

# solution 1
result = []
for c1 in string1:
    # print(c1)
    for c2 in string2:
        # print(c2)
        # print(c1, c2)
        print(c1+c2)
        result.append(c1+c2)

print(result)
print("=================")


# solution 2
result = [[c1+c2 for c1 in string1] for c2 in string2]
print(result)


result = [c1+c2 for c1 in string1 for c2 in string2]
print(result)