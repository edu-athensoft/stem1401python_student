"""
Write program to find the first appearance of the substring 'not'
and 'poor' from a given string, if 'not'  follows the 'poor', replace
the whole 'not'...'poor' substring with good
"""
# this is homework 1
# homework 2 -> revise the errors meaning
my_string = input("Input your string (must include not poor or not...poor): ")
index_not = my_string.index("not")
index_poor = my_string.index("poor")
final_str = my_string.replace(my_string[int(index_not): int(index_poor) + len("poor")], "good")
print(final_str)