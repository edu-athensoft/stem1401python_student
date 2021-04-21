"""
file mode

mode letter(s) indicates the operation on files
mode code:

Group 1.
r       open file for reading
w       open file for writing
a       open file for appending
x       open file for creating

Group 2.
t       open a text file
b       open a binary file

Group 3.
+       plus

r+
w+

Combination
rt      read, text file
wt      write,text file
rb
wb
...

r+b
r+t

Default
rt  => r
rt  => default

"""

# import os
# import os.path
try:
    print("Start opening file...")
    filepath = "../day10_201114/review1.py"
    print("\t"+filepath)
    file = open(filepath, 'rt')

    print("Closing...")
    file.close()

except FileNotFoundError as fe:
    print(fe)

except IOError as ioe:
    print(ioe)

except Exception as e:
    print(e)

print("Done.")


"""
4AAQSkZJRgABAQEAYABgAAD/4QAiRXhpZgAATU0AKgAAAAgAAQESAAMAAAABAAEAAAAAAAD/2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEB
AMFBwYHBwcGBwcICQsJCAgKCAcHCg0KCgsMDAwMBwkODw0MDgsMDAz/2wBDAQICAgMDAwYDAwYMCAcIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDA
wMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAz/wAARCABNAIkDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8Q
AtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdI
SUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4
+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBh
JBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goO
EhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEA
PwD8DolwOmKs2xxUCL8v1q7BDlcZ/OuiKMZvUuWcmSMtt9quQN50wXniqkSbh8vpit/wr4H1LXnZrW1mkVUaRnC/KqgEkk+gAJ+gNHL2OUrXx
2w7c9qyZ7XA3NXV6n4FvLUp9oVbfzFDASHaVyCRkH6H9PWqVz4AuZ4FkRpJDvAIWM8A/wBev5U4xZtGMjAhtNwzUggwK7PTPgtqWpaes1rNby
qxbA34O1eS35c1keJvAGteDpZE1LT7i28uZoPnQrllxkc+mRRqacstz7j/AOCMWkSaz4L+JFp5dqsdwbbbcFP30RAkypYHO0/KceoNdNoPxb8S/
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

"""