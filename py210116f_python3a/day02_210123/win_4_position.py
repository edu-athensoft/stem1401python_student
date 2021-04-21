"""
set position for a window
dimension

"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - setting init position')

# setting size
# x must be written in lower case
root.geometry('640x480+300+200')

root.geometry('640x480-300+200')

root.geometry('640x480+300-200')

root.geometry('640x480-300-200')

# anti-pattern
# root.geometry('640X480+300+200')

root.mainloop()


