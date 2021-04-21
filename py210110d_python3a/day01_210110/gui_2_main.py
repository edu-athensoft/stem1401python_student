"""
my first GUI program
Tkinter

create a title for main window
"""

# import tkinter
from tkinter import *

try:
    root = Tk()
    root.title('Python GUI - My First GUI App')

    # 4:3 ratio
    # root.geometry('640x480')
    # root.geometry('800X600')
    root.geometry('800x600')

    # 16:9 ratio
    root.geometry('1600x900')


    root.mainloop()

except TclError as te:
    print(te)

except Exception as e:
    print(e)

