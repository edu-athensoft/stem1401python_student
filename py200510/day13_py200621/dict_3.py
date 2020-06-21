"""
dictionary - add or update element

We can add new items or change the value of existing items using assignment operator '='.

"""

stu1 = {"name": "Jackie", "age": 26}
print(stu1, type(stu1))

# update
print("=== update ===")
stu1["name"]="Peter"
print(stu1)
print("name" in stu1)

# add
print("=== add ===")
print("before","score" in stu1)
stu1["score"]=98
print(stu1)
print("after","score" in stu1)
