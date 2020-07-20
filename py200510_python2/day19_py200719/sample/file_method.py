"""
Python File Methods

There are various methods available with the file object.
Here is the complete list of methods in text mode with a brief description.

Methods
close()
Close an open file. It has no effect if the file is already closed.

detach()
Separate the underlying binary buffer from the TextIOBase and return it.

fileno()
Return an integer number (file descriptor) of the file.

flush()
Flush the write buffer of the file stream.

isatty()
Return True if the file stream is interactive.

read(n)
Read at most n characters from the file. Reads till end of file if it is negative or None.

readable()
Returns True if the file stream can be read from.

readline(n=-1)
Read and return one line from the file. Reads in at most n bytes if specified.

readlines(n=-1)
Read and return a list of lines from the file. Reads in at most n bytes/characters if specified.

seek(offset,from=SEEK_SET)
Change the file position to offset bytes, in reference to from (start, current, end).

seekable()
Returns True if the file stream supports random access.

tell()
Returns the current file location.

truncate(size=None)
Resize the file stream to size bytes. If size is not specified, resize to current location.

writable()
Returns True if the file stream can be written to.

write(s)
Write string s to the file and return the number of characters written.

writelines(lines)
Write a list of lines to the file.


"""