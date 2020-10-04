"""
file operation

step 1. open file
step 2. operation on file (read/write)
step 3. close file

"""

# how to open a file at specified location

f = None
try:
    f = open("D:\workspace\pycharm201803\stem1401python_student\py200912f_python2m7\day04_201003\homework\homework_question_1.py")
    # py200912f_python2m7/day04_201003/homework/homework_question_1.py

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    f.close()
