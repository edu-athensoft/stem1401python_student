"""
mode
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
"""

try:
    file = open('mynewfile.log','x')
    file.close()

except IOError as ioe:
    print(ioe)
except Exception as e:
    print(e)

else:
    print("A new file created.")
