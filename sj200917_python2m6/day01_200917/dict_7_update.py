"""
dictionary
update()

"""


dict1 = {1: "one", 3: "three"}
dict2 = {2: "two"}

# dict1.update(dict2)
# print(dict1)


# keep original dataset
result_dict = dict1.copy()
result_dict.update(dict2)
print(result_dict)

# update -> check if item(k-v) does exist, overwrite, else add


# ex 1.
card1 = {1: 'SS1', 2:'S1', 3:'A1'}
card2 = {4: 'SS2', 5:'SS3', 6:'S2'}

# how to form a team card set?







