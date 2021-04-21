"""
Clock: v1

NOTE: root = window

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
review datetime
1. to get current date and time
Sample code:
now = datetime.datetime.now()
print(now)
2. to get string form of the datetime object

show datetime and milli-second


from datetime import datetime
# print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))

"""


from time import *
from tkinter import *
from datetime import *


def time_label():
    # current_time = strftime('%H: %M: %S %p')
    # current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    current_time = datetime.now().strftime('%a %H:%M:%S.%f')[:-3]
    clock_label.config(text=current_time)
    clock_label.after(10, time_label)

# main program
root = Tk()
root.title("Python GUI - Clock label")
root.geometry("{}x{}+200+240".format(640, 200))
root.configure(bg="crimson")
root.resizable(0, 0)

# label object
clock_label = Label(root,
              bg = "goldenrod",
              fg = 'white',
              height = 3,
              width = 20,
              font = "Helvetic 20 bold")
clock_label.pack(anchor="center", ipadx=20, ipady=20)

time_label()

root.mainloop()
