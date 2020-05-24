"""
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

pick out the names who are outside quebec for 183 days
"""

# namelist
namelist = [('Peter',0),('Marie',1),('Sarah',0),("Jack",1)]

# outside_qc = []

# list()
data = list(filter(lambda x: x[1] == 0, namelist))
print(data)

#
print(dict(data))