"""
stem1402_python_homework_4_steven
"""

# 1.
list1 = ['MON','TUE','WED','THU','FRI','SAT','SUN']
list2 = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']


mydict = dict(zip(list1, list2))
print(mydict)
print()
print("-----------------------------------------------------------------------------------------------------------------")


# 2.

dict1 = {"92%": "22 years old", "100%": "24 years old", "87%": "21 years old", "96%": "23 years old", "94%": "22 years old"}

res = dict(sorted(dict1.items(), key=lambda x: x[1]))
print(f"Sorted in ascending order by age : {res}")


res = dict(sorted(dict1.items(), key=lambda x: x[0], reverse=True))
print(f"Sorted in descending order by score : {res}")
print()
print("-----------------------------------------------------------------------------------------------------------------")



# 3.
def vote(a,b,c):
    return a+b+c

dict1 = {
    "Jason": vote(300, 360, 270),
    "Bill": vote(280,340,291),
    "William": vote(350, 310, 324)
}

max = 0
res = dict1.values()

for i in res:
    if i > max:
        max = i
print(f"{max} is the highest vote number")









