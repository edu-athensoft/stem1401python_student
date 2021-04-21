"""
to permanently persist into external storage

1. write a program to save any text-based content
"""

# step 1. prepare data to output
data = "This is the 2nd part of content I would like to save."

# step 2. writing
file = open("mydata.txt",'w')
file.write(data)
file.close()






