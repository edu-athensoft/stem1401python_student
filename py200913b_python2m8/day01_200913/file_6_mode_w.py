"""
1. Open (with a mode)
2. R/W
3. Close

write a file
mode: w

open()
write()

try-except-finally
close()

text content is multiple line string

conclusion:
The mode of 'w' create a new file if it does not exist.
or it will truncate the old file and rewrite with new content.

"""

# case 1. truncating
# by zeyue
'''
try:
    f = open("file_6_mode_w.txt", "w")
    content = """This is the new content of file_6_mode_w.txt.
    This is the second line of the file."""
    charnum = f.write(content)
    print(f"{charnum} has been written in the file: file_6_mode_w.txt")

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    f.close()
'''

# case 2. create new file and write
# by zeyue

try:
    f = open("file_6_mode_w2.txt", "w")
    content = """This is the new content of file_6_mode_w.txt.
    This is the second line of the file."""
    charnum = f.write(content)
    print(f"{charnum} has been written in the file: file_6_mode_w2.txt")

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    f.close()


# case 3. write a logging application
# file name: log.txt/log.py
# input a sentence by user from his/her keyboard
# save the words into the log file

# zeyue
try:
    f = open("log.txt", "w")
    content = input("Input a sentence")
    charnum = f.write(content)
    print(charnum)

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    f.close()



# kevin
try:
    f = open("log", "w")

    content = input("Enter what you want to add: ")
    charnum  = f.write(content)
    print(f"{charnum} has been writing in file: log")

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    f.close()


# guangzhu
try:
    x = open('log.txt','w')
    content = input('please enter something:')

    a = x.write(content)
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    x.close()



'''
# guangzhu
try:
    x = open('file_6_mode_w.txt', 'w')
    content = "write a lot of things " \
              "bla bla bla" \
              "cool"

    a = x.write(content)
    
except Exception as e:
    print(e)
    
except FileNotFoundError as fe:
    print(fe)
    
finally:
    x.close()



# by kevin
try:
    f = open("file_6_mode_w","w")

    content = """this is the new content
    to change. Idk what to write lol"""
    charnum  = f.write(content)

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    f.close()

'''


