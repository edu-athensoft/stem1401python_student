# homework 3

# 1

list1 = ['MON','TUE','WED','THU','FRI','SAT','SUN']
list2 = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
dictionary = dict(zip(list1, list2))
print(dictionary)


# 3

d = {"name":"Jason", "voted1":300, "voted2":360, "voted3":270}
d1 = {"name":"Bill", "votde1":280, "voted2":340, "voted3":291}
d2 = {"name":"William", "votde1":350, "voted2":310, "voted3":324}

# Jason
value = list(d.values())
score1 = value[1] + value[2] + value[3]
print("Jason have {}".format(score1))

# Bill
value = list(d1.values())
score2 = value[1] + value[2] + value[3]
print("Bill have {}".format(score2))

# William
value = list(d2.values())
score3 = value[1] + value[2] + value[3]
print("William have {}".format(score3))


max_num = max(score1, score2, score3)

if max_num == 984:
    print("William is the president")
elif max_num == 911:
    print("Bill is the president")
else:
    print("Jason is the president")