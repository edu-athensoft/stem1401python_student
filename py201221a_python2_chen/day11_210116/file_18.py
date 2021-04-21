"""
to write multiple lines into a file - (overwrite)

writing to files

write()

'w' - we can write content into the file; and if there is no file existing, then just create the file first.

'a'

'x'

"""


# step 1.
file = open('text18.txt','w')

# step 2. to prepare the content to save
content = """line 1 alsdjfalsjflasfjaslfjaksfdasf
line 2 alsdjfalsjflasfjaslfja
line 3 alsdjfalsjflasfjaslfja
"""

content = 'line 1 alsdjfalsjflasfjaslfjaksfdasf\nline 2 alsdjfalsjflasfjaslfja\nline 3 alsdjfalsjflasfjaslfja'

# step 3. to perform writing
file.write(content)

# step 4. to close
file.close()