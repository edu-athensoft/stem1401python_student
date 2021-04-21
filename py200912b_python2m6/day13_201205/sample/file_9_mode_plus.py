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
f = None
try:
    f = open("file9_mode_plus.txt",'r+')

    for line in f:
        print(line, end="")

    content = "this is the new content to write\n"
    charnum = f.write(content)
    print(f"charnum={charnum}")

    f.close()

except FileNotFoundError as e:
    print(e)

except Exception as e:
    print(e)
# finally:
    # f.close()








