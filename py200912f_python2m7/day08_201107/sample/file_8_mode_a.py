"""
Mode	Description
'r'	    Open a file for reading. (default)
'w'	    Open a file for writing.
        Creates a new file if it does not exist or truncates the file if it exists.
'x'	    Open a file for exclusive creation.
        If the file already exists, the operation fails.
'a'	    Open for appending at the end of the file without truncating it.
        Creates a new file if it does not exist.
't'	    Open in text mode. (default)
'b'	    Open in binary mode.
'+'	    Open a file for updating (reading and writing)
"""

# demo
# 1st. create file and the file does not exist before creating
f = open("file8_mode_a.txt",'a')

content = "this is the new content to write\n"
charnum = f.write(content)
f.close()

print(f"charnum={charnum}")

# log
# time host ip operation, operator, message


