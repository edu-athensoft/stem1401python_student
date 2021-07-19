"""
Set Operation
Intersection
get common items
"""

# Set Intersection Operation
# case 1.
set1 = {1,2,3}
set2 = {4,5,6}
set_result = set1 & set2
print('Set Intersection Operation - case 1: ',set_result)


# case 2.
set1 = {1,2,3}
set2 = {3,4,5}
set_result = set1 & set2
print('Set Intersection Operation - case 2: ',set_result)


# case 3.
set1 = {1,2,3}
set2 = {1,2,3}
set_result = set1 & set2
print('Set Intersection Operation - case 3: ',set_result)

# case 1b.
set1 = {1,2,3}
set2 = {3,4,5}
set_result = set1.intersection(set2)
print('Set Intersection Operation - case 1b: ',set_result)

set_result = set2.intersection(set1)
print('Set Intersection Operation - case 1b: ',set_result)

# application
tour_class1 = {'Stockholm','Paris','Bergen','Paris', 'Bergen','New York'}
tour_class2 = {'Boston','Washington','New York','New York'}
spot_set = tour_class1 & tour_class2
print(spot_set)