"""
writing to files
write()

'w' - we can write content into the file; and if there is no file existing, then just create the file first.

'a'

'x'

"""


# step 1.
file = open('text17a.txt','w')

# step 2. to prepare the content to save
content = 'line 1 alsdjfalsjflasfjaslfjaksfdasf'

# step 3. to perform writing
file.write(content)

# step 4. to close
file.close()