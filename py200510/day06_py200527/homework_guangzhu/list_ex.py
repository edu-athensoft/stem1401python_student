
# print(list(map(lambda x: x*2, [1,2,4])))

list = ['abc', 'xyz', 'aba', '1221']

# print(list(map(lambda x: x*2, [1,2,4])))

a = 0
for string in list:
    if len(string) > 1 and string[0] == string[-1]:
        a += 1
print(a)

print()
x = input('Please input a list:')
print(x,x)

# Loop the first list to check if it contains a second list, then return true or false.

