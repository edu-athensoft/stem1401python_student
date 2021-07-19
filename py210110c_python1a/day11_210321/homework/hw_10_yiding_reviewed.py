"""

q6. 
"" double quotes, 
''single quote, 
""" """ triple quote for multiple-line string


q7. 
name1 = 'U+00A9 2019 copyrights'
print(name1)

q8. print(string1)
    print(string2)

q9. string1 = "abc'xyz"mn\pq\nabc"
    print(string1)

q10. It gives: True 1
"""

# q7
name1 = 'U+00A9 2019 copyrights'
print(name1)

name1 = '\u00A9 2019 copyrights'
print(name1)

# q8
# print(string1)
# print(string2)

# string1 = ''
# string2 = ''
# print(string1)
# print(string2)

print("====")
print()
print("====")

# q9
# string1 = "abc'xyz"mn\pq\nabc"
# print(string1)

string1 = """abc\'xyz\"mn\\pq\\nabc"""
print(string1)

string1 = "abc\'xyz\"mn\\pq\\nabc"
print(string1)

string1 = r"abc'xyz'mn\pq\nabc"
print(string1)


# q10
print(1==True, 1+False)
# output:  True  1


