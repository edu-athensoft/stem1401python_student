"""
file writelines()

readlines()
    - built-in
    - user-defined function/method
    - third party methods

what object does this method belongs to?
    - find or create the object

result type?
    - primitive type (number, str) and collection type
    - other type with api?
    - other type convert to primitive type or collection type

processing data and manipulating data with logic
"""

"""
dict1 = {
    1: 11,
    2: 22,
}

for v in dict1.values():
    print(v)

print(type(dict1.values()))
result = list(dict1.values())
print(result,type(result))
"""


file = open("mytext.txt", "w+")
lines = ["1111\n", "2222\n", "daaa\n"]
# lines = "sss"
print(lines, type(lines))
file.writelines(lines)
file.close()

# conclusion
# case 1.
# lines = "abcdedf"
# writelines() can write a string directly

# case 2.
# lines = "abcdedf", "ddd", "daaa"
# writelines() accepts tuple

# case 3.
# lines = ["abcdedf", "ddd", "daaa"]
# writelines() accepts list

# case 4.
# clean/truncate and write

# case 5.
# why the contents are not presented write by line?
# append \n











