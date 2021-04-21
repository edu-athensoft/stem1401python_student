"""
[Homework]
Date: 2021-03-08
1. Write a GUI program of clock
Requirements:
(Function)
Show current time in the pattern of HH:mm:ss.aaa
i.e.
10:12:45.369
(UI)
Display a title, main area for clock, and footer for the date
Due date: by the end of next Friday
Hint:
import datetime
strftime
"""

"""
score:
footer, improper size of font (-2)

"""

from tkinter import *
from tkinter.ttk import Separator
import datetime

def count():
    clock_label.config(text=datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3])
    clock_label.after(1, count)

# main program
root = Tk()
root.title('Python GUI - Label clock')
root.geometry("{}x{}+200+240".format(640, 540))
root.configure(bg='#ddddff')

# title label object
label1 = Label(root, text="Label Clock", bg="blue", fg="white", height=2, width=100, font="Helvetic 35 bold")
label1.pack()

# separator
sep1 = Separator(root, orient=HORIZONTAL)
sep1.pack(fill=X)

# clock label object
clock_label = Label(root,
                    bg="seagreen",
                    fg='white',
                    height=8,
                    width=100,
                    font="Helvetic 30 bold")
clock_label.pack()

# separator
sep1 = Separator(root, orient=HORIZONTAL)
sep1.pack(fill=X)

# footer label object
label2 = Label(root, text="Version 1 | Ze Yue Li | 2021-03-08", bg="red", fg="white", height=2, width=100, font="Helvetic 35 bold")
label2.pack()

count()

root.mainloop()
