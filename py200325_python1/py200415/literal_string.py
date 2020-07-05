"""
string literal
"""

# case 1: normal string with ", '
strings = "This is Python"
strings2 = 'This is Python'
print("strings",strings)
print("strings2",strings2)

# case 2
char = "C"
char = 'C'
print("char",char)

# case 3
multiline_str = """This is a multiline string with more than one line code."""
print(multiline_str)

multiline_str = """66666 This is a multiline string 
    with more than one line code.
  ksdjfasdfaskdf asdfjas dfas f sdf as dfas"""
print(multiline_str)

multiline_str = '''66666 This is a multiline string 
    with more than one line code.
  ksdjfasdfaskdf asdfjas dfas f sdf as dfas'''
print(multiline_str)


# case 4:  escaped character
print("This is a multiline string. It is powerful")
print("This is a multiline string. \n It is powerful")
# new line   \n
# \\
# \'
# \"
# \n
# \t
print("This is a quote like \" ")
print("This is a quote like \' ")
print("This is a quote like \t is a quote like \t is a quote")

# case 5: unicode
unicode = u"\u00dcnic\u00f6de"

copywrite = "Copyright. \u00A9 All rights reserved"
print(copywrite)

ibmtm = "IBM \u2122"
print(ibmtm)

# case 6: raw string
raw_str = r"raw \n string"
print(raw_str)


