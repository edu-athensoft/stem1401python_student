"""
literal string

prefix and suffix
redo
reuse
remark
remaster
re- prefix

swim - swimming
run - running
jump - jumping
-ing suffix

"""
# unicode charset (utf-8)
# u -> prefix
string1= u"\u00dcnic\u00f6de"
print(string1)

string1= u'\u00dcnic\u00f6de'
print(string1)
# unicode
# \u00dc

# GB2312
# J
# BIG5
# ISO-8859-1
# latin-1

print(0x00dc)
print(0x00f6)

# Greek char Pi
string2 = u"\u03A0"
print(string2)

# Greek char Sigma
string2 = u"\u03A3"
print(string2)



# escape character
string11 = '\''
print(string11)

string12 = '\"'
print(string12)

print("==========")
string13 = 'abc\n\nabc'
print(string13)
print("==========")

string14 = 'abc\tddd'
print(string14)

string14 = 'a\tddd\tx\ty'
print(string14)

string14 = 'b\tddd\tu\tv'
print(string14)

string15 = '\\'
print(string15)


