"""
for-loop
"""

"""
12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60
12 x 6 = 72
12 x 7 = 84
12 x 8 = 96
12 x 9 = 108
12 x 10 = 120

for-loop
string.format()
"""


# kevin

string_template = "12 x {} = {}"

for i in range(1,11):
    print(string_template.format(i, 12 * i))

print()


# qichun
str_temp = "12 x {} = {}"
for i in range(1,12):
    print(str_temp.format(i, 12 * i))

