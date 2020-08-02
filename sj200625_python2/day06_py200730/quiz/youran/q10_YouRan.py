"""
find words that are too long
"""
string1 = "The man woman dog cat flower bobcat"
list1 = string1.split()
list2 = []
limit = int(input("Input limit: "))

for i in list1:
    if len(i) > limit:
        list2.append(i)

print(list2)
