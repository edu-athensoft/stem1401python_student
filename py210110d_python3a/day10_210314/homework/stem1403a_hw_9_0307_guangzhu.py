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
footer is not completed shown (-5)
code cannot be reached in def clock_count()  (-5)

"""

from tkinter import *
from tkinter.ttk import Separator
import datetime
# main program
root = Tk()
root.title('Time clock')
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')
def clock_count():
    time = datetime.datetime.now().strftime('%H:%M:%S:%f')[:-3]
    clock.config(text=time)
    clock.after(1,clock_count)
    root.update()   ### cannot be reached

# label object
title_label = Label(root,text='Time clock', bg='navy', fg='snow', height=2, width=50, font='Roman 24 bold')
title_label.pack(side=TOP)
sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X)
clock = Label(root,
              bg = "seagreen",
              fg = 'white',
              height = 5,
              width = 50,
              font = "Helvetic 48 bold",relief='groove')
clock.pack()
sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X)
footer_label = Label(root, text='Version 1, Guang Zhu, 13/03/2021', bg='snow', fg='PeachPuff3', width=50, height=2, font='Roman 24 bold')
footer_label.pack(side=BOTTOM)
clock_count()

root.mainloop()
