"""
string formatting

truncating string with format()
"""
str1 = "caterpillar"
print(str1)

result = str1[:3]
print(result)

print("{:.3}".format(str1))

print("|{:*^7.3}|".format(str1))