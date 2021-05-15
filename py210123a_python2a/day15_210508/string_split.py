"""
String

split()
"""




# case 1. no parameters
str1 = "This  is   a  demo program."
result = str1.split()
print(type(result))

for item in result:
    print(f'|{item}|')

print(result)


# case 2. abc, abf, bbc, acb, ddf
str2 = "abc, abf, bbc, acb, ddf"
result = str2.split(',')
print(type(result))

for item in result:
    print(f'|{item}|')

print(result)


# case 2b. remove all white spaces
str2 = "abc, abf, bbc, acb,  ddf"
result = str2.split(', ')
print(type(result))

for item in result:
    print(f'|{item}|')

print(result)

# case 2c. remove all white spaces
str2 = "abc, abf, bbc, acb,  ddf"
result = str2.split(',')
print(type(result))

strlist = []
for item in result:
    print(f'|{item.strip()}|')
    strlist.append(item.strip())

print(strlist)




