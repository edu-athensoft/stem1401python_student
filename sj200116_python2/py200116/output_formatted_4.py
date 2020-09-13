"""
formatted output
keyword parameter
"""

# Lily, Mary
name1 = 'Lily'
name2 = 'Mary'

story = "{name1} and {name2} went to the cinema last week."

print(story.format(name1 = name1,  name2 = name2))
print(story.format(name2 = name2,  name1 = name1))
