"""
to permanently persist into external storage

to append content to an existing file

write a program to save any text-based content
"""

# step 1. prepare data to output
print("Program started.\n")
data = "This is the 4th part of content I would like to save as a new line.\n"

# step 2. writing
print("Writing...")
print(f"Data: {data}\n")
file = open("mydata.txt",'a')
file.write(data)
file.close()

print("Done.")






