"""
homework

create a base dir
create at least 3 subdir
rename these 3 subdir to any other names respectively
print out result

"""

import os


try:
    path = '../day11/base_dir'
    os.mkdir(path)

except OSError as oe:
    print(oe)

except RuntimeError as rte:
    print(rte)

except Exception as e:
    print(e)


try:
    path_2 = 'base_dir/sub_dir_1'
    os.mkdir(path_2)

except OSError as oe:
    print(oe)

except RuntimeError as rte:
    print(rte)

except Exception as e:
    print(e)


try:
    path_3 = 'base_dir/sub_dir_2'
    os.mkdir(path_3)

except OSError as oe:
    print(oe)

except RuntimeError as rte:
    print(rte)

except Exception as e:
    print(e)


try:
    path_4 = 'base_dir/sub_dir_3'
    os.mkdir(path_4)

except OSError as oe:
    print(oe)

except RuntimeError as rte:
    print(rte)

except Exception as e:
    print(e)


print("Old subdirectories: ", os.listdir("./base_dir"))

old_name_sub_dir_1 = "base_dir/sub_dir_1"
new_name_sub_dir_1 = "base_dir/new_sub_dir_1"
old_name_sub_dir_2 = "base_dir/sub_dir_2"
new_name_sub_dir_2 = "base_dir/new_sub_dir_2"
old_name_sub_dir_3 = "base_dir/sub_dir_3"
new_name_sub_dir_3 = "base_dir/new_sub_dir_3"

os.rename(old_name_sub_dir_1, new_name_sub_dir_1)
os.rename(old_name_sub_dir_2, new_name_sub_dir_2)
os.rename(old_name_sub_dir_3, new_name_sub_dir_3)


print("New subdirectories: ", os.listdir("./base_dir"))
