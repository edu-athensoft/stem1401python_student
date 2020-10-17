"""
1. Map two lists into a dictionary for day of week
list1 = ['MON','TUE','WED','THU','FRI','SAT','SUN']
list2 = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
"""
# the lists
list1 = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
list2 = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
# the dictionary
my_dict = {}
# convert lists to method
for key in list1:
    for value in list2:
        my_dict[key] = value
        list2.remove(value)
        break
# output
print(f"The dictionary is: {my_dict}")

# or

# the lists
list_1 = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
list_2 = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
# put both lists together and convert
my_dict_2 = dict(zip(list_1, list_2))
# output
print(f"The dictionary is: {my_dict_2}")

