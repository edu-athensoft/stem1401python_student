"""
stem1402_python_homework_3_steven
"""

# 1.
mydict = {1: 'a',
          2: 'b',
          3: 'c',
          4: 'd',
          5: 'e'}

mydict2 = {}

if len(mydict) == 0:
    print(f"{mydict} is an empty dictionary")
else:
    print(f"{mydict} is not an empty dictionary")
print()
print("---------------------------------------------------------------------")

# 2.
n = int(input("Please enter the amount of square numbers you wish to know:"))
mydict = {k: k*k for k in range(1,n+1)}
print(mydict)
print()
print("---------------------------------------------------------------------")

# 3.

dict1 = {
    'Justin': 20,
    'Julian': 19,
    'Jimmy': 10,
    'Javier': 11,
    'Jonathan': 5
}

res = list(dict1.values())
max = 0

for i in res:
    if i > max:
        max = i
print(f"The maximum value in {dict1} is {max}")
print()

min = 0

for i in res:
    if i < max:
        min = i
print(f"The minimum value in {dict1} is {min}")







