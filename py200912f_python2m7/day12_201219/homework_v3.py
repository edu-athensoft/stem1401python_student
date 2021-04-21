"""

design a loop
for the case of determined iteration, use for loop

choose the data structure for the loop

"""

import os

# old_name_sub_dir_1 = "base_dir/sub_dir_1"
# new_name_sub_dir_1 = "base_dir/new_sub_dir_1"
# old_name_sub_dir_2 = "base_dir/sub_dir_2"
# new_name_sub_dir_2 = "base_dir/new_sub_dir_2"
# old_name_sub_dir_3 = "base_dir/sub_dir_3"
# new_name_sub_dir_3 = "base_dir/new_sub_dir_3"

base = "base_dir"

listold = ("sub_dir_1","sub_dir_2","sub_dir_3","sub_dir_4")
listnew = ("new_sub_dir_1","new_sub_dir_2","new_sub_dir_3","new_sub_dir_4")


dir_namepairs = []

for i in range(len(listold)):
    print(listold[i],listnew[i])
    dir_namepairs.append((listold[i],listnew[i]))

print(dir_namepairs)

# dir_namepairs = (("sub_dir_1","new_sub_dir_1"),
#                  ("sub_dir_2","new_sub_dir_2"),
#                  ("sub_dir_3","new_sub_dir_3"))

for oldname,newname in dir_namepairs:

    oldname = base + "/" + oldname
    newname = base + "/" + newname
    print(oldname, newname)
    # os.rename(oldname, newname)