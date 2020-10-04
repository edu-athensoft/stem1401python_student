"""
Read and Write Mode
In mode, we specify whether we want to read 'r', write 'w' or append 'a' to the file.

Text and Binary Mode
We also specify if we want to open the file in text mode or binary mode.
t: text mode
b: binary mode

open(),   rt  mode = read, text mode


"""

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