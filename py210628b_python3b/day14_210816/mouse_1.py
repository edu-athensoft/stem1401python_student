"""
Create a window
Display coordinate (x, y) of mouse cursor when you click the LB

Expected result:
clicked at (45, 60)
clicked at (105, 348)
"""

from tkinter import *


def handler(event):
    print(f'clicked at ({event.x}, {event.y})')


root = Tk()
root.title("Event Handling")
root.geometry("640x480+300+300")
root.config(bg="#ddddff")

# test left mouse button   (LMB)
root.bind('<Button-1>', handler)

root.mainloop()
