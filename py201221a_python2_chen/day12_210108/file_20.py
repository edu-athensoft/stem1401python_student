"""
how to append content to existing file(s)

the previous content will be kept
the new content will be added to the tail

'a'

when to use this mode?
1. for logging,  writing log file
purpose of log file is to traceback or audit

2. for keeping previous content


"""

file = open("datasource.txt", 'a')
content = "new line 1\nnew line 2"
file.write(content)
file.close()




