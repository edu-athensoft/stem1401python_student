"""
Set operation
Union
"""


# Set Union Operation
# case 1.
set1 = {1,2,3}
set2 = {4,5,6}
set_result = set1 | set2
print('Set Union Operation - case 1: ',set_result)

# case 2.
set1 = {1,2,3}
set2 = {3,5,6}
set_result2 = set1 | set2
print('Set Union Operation - case 2: ',set_result2)

# case 3.
set1 = {1,2,3}
set2 = {1,2,3}
set_result3 = set1 | set2
print('Set Union Operation - case 3: ',set_result3)

# case 1b.
set1 = {1,2,3}
set2 = {4,5,6}
set_result = set1.union(set2)
print('Set Union Operation - case 1b: ',set_result)

set1 = {1,2,3}
set2 = {4,5,6}
set_result = set2.union(set1)
print('Set Union Operation - case 1b: ',set_result)

# application
tour_class1 = {'Stockholm','Paris','Bergen','Paris', 'Bergen'}
tour_class2 = {'Boston','Washington','New York','New York'}
spot_set = tour_class1 | tour_class2
print(spot_set)