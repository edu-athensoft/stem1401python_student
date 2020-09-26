"""
stem1402_python_homework_2_steven
"""

# 1.

n = int(input("Please enter the amount of square numbers you wish to know:"))

charcount = {}
counter = 1

while counter <= n:
    if counter not in charcount:
        charcount[counter] = counter*counter
        counter += 1

print(charcount)
print()
print("---------------------------------------------------------------------------")


# 2.

dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}
dict4 = {}

for i in (dict1, dict2, dict3):
    dict4.update(i)

print(f"{dict1}, {dict2} and {dict3} all added together = {dict4}" )
print()
print("---------------------------------------------------------------------------")


# 3. I didn't succeed on this question

person_profile = {
    'empid': '0001',
    'name': 'Peter',
    'ismanager': True,
    1: 'availabe',
    2: 'long-term'
}


for i in person_profile:
    print(type(i))
    if type(i) == "<class 'int'>":
        person_profile.pop(i)

print(person_profile)









