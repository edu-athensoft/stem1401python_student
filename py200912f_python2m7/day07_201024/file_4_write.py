"""
to permanently persist into external storage

to append content to an existing file

write a program to save any text-based content

1. can append
2. no '\n' by default


"""

# step 1. prepare data to output
data = "This is the 3rd part of content I would like to save."

# step 2. writing
file = open("mydata.txt",'a')
file.write(data)
file.close()






