"""
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
footer is missing (-10)
code cannot be reached in def clock_count()  (-5)

file name (-1)
"""


from tkinter import *
from tkinter.ttk import Separator
import datetime

root = Tk()
root.title('Chengjun’s Clock')
root.geometry("{}x{}+200+200".format(640, 480))
root.configure(bg='#ddddff')


def clock_count():
    time = datetime.datetime.now().strftime('%H:%M:%S:%f')[:-3]
    clock.config(text=time)
    clock.after(1,clock_count)
    root.update()
    ### cannot be reached

title_label = Label(root,text='Clock', bg='red', fg='snow', height=1, width=60, font='Roman 36 bold')
title_label.pack(side=TOP)
sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X)
clock = Label(root,
              bg = "seagreen",
              fg = 'white',
              height = 6,
              width = 50,
              font = "Helvetic 48 bold",relief='groove')
clock.pack()


clock_count()
root.mainloop()