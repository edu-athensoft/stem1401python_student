"""
formatted output
positional parameter
string format()
"""

# Lily, Mary
name1 = 'Lily'
name2 = 'Mary'

story = "{} and {} went to the cinema last week."

print(story.format(name1, name2))

# reverse the names
# option 1
print(story.format(name2, name1))

# option 2
story = "{1} and {0} went to the cinema last week."
print(story.format(name1, name2))