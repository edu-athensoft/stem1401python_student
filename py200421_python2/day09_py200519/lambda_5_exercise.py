"""
list1 = [0,1]
183 days
0: outside quebec
1: stay in quebec

mystatus = {
    "peter" : 0,
    "marie" : 1,
    "sarah": 0,
    "Jack" : 1,
    ...
}

pick out the names who are outsite quebec for 183 days
"""

# 500 persons
mystatus = {
    "peter" : 0,
    "marie" : 1,
    "sarah": 0,
    "Jack" : 1
}

temp = list(mystatus)
print(temp)

namelist = [
    ["peter", 0],
    ["marie" , 1],
    ["sarah", 0],
    ["Jack" ,1]
]

print(namelist)

outside_qc_list = list(filter(lambda x: x[1]==0, namelist))
print(dict(outside_qc_list))



