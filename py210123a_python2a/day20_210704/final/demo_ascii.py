"""

"""

# get a list of ascii number
cipher_text = "84 104 105 115 32 105 115 32 97 32 112 121 116 104 111 110 32 115 111 117 114 99 101 32 99 111 100 101 46 "
list1 = list(cipher_text.split())
# print(list1)

# using chr() to convert a ascii number to a char
result = ''
for num in list1:
    result += chr(int(num))

print(result)

print("=====================")

ascii_map = {'84': "T",
             '104': "h",
             '105': "i",
             '115': "s",
             '32': " ",
             '97': "a",
             '112': "p",
             '121': "y",
             '116': "t",
             '111': "o",
             '110': "n",
             '117': "u",
             '114': "r",
             '99': "c",
             '101': "e",
             '100': "d",
             '46': "."}

result_list = []

for char in list1:
    result_list.append(ascii_map[char])

result = ''.join(result_list)
print(result)
