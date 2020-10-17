"""
2. Create a dictionary properly and sorting by age in ascending order, then sorting by score in descending order.
Both results are required to print out.
name	age	score
Amy	    22	92
Lily	24	100
Sandy	21	87
Peter	23	96
Jack	22	94
"""

# the dictionary

age_dict = {"Amy": 22, "Lily": 24, "Sandy": 21, "Peter": 23, "Jack": 22}
score_dict = {"Amy": 92, "Lily": 100, "Sandy": 87, "Peter": 96, "Jack": 94}

# ascending age

# get the values
age = lambda item: item[1]
# sorting
sorted_ages_list = sorted(age_dict.items(), key=age)
# convert into dictionary
sorted_ascending_ages_dict = dict(sorted_ages_list)
# output
print(f"The sorted by ages in ascending order dictionary is: {sorted_ascending_ages_dict}")

# descending score

# get the values
score = lambda item: item[1]
# sorting
sorted_scores_list = sorted(score_dict.items(), key=score, reverse=True)
# convert into dictionary
sorted_descending_scores_dict = dict(sorted_scores_list)
# output
print(f"The sorted by scores in descending order dictionary is: {sorted_descending_scores_dict}")

