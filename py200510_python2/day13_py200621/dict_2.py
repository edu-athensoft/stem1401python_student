"""
access element
"""

stu1 = {"name": "Jackie", "age": 26}
print(stu1, type(stu1))


# obtain the name of stu1 via []
stu1_name = stu1["name"]
print(stu1_name)
print(stu1["name"])
print()

# obtain the age of stu1 via []
stu1_age = stu1["age"]
print(stu1_age)
print(stu1["age"])
print()


print("=== get() ===")
# using get()
stu1_name = stu1.get("name")
print(stu1_name)

# using get()
stu1_age = stu1.get("age")
print(stu1_age)


# get() v.s []
print(stu1.get("score"))
print(stu1)
print()

# KeyError: 'score'
print(stu1["score"])
print(stu1)
