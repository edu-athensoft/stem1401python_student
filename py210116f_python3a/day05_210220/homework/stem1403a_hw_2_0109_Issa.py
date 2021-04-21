"""
[Homework]
Date: 2021-02-06
1. Try out label widget
Description:
- create a window based on previous homework
- set icon, title, dimension, maxsize, minsize, bg and any other options for the window as much as you know
- create a text Label
"""

import tkinter as tk
import time

root = tk.Tk()

root.title("Basketball")

root.iconbitmap("./Basketball.ico")

window_width = 400
window_height = 225

screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()

x = int(screenwidth/2 - window_width/2)
y = int(screenheight/2 - window_height/2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.maxsize(1600, 900)

root.minsize(320, 180)

my_label = tk.Label(root, text="Please do not close this window before it becomes black!")
my_label.pack()

my_label = tk.Label(root, text="Thanks!")
my_label.pack()

my_btn = tk.Button(root, text="Close", command=root.destroy)
my_btn.pack()

root.attributes("-topmost", True)

root.config(bg="black")
root.update()
time.sleep(1.5)

root.config(bg="coral1")
root.update()
time.sleep(1.5)

root.config(bg="coral2")
root.update()
time.sleep(1.5)

root.config(bg="coral3")
root.update()
time.sleep(1.5)

root.config(bg="PaleVioletRed1")
root.update()
time.sleep(1.5)

root.config(bg="PaleVioletRed2")
root.update()
time.sleep(1.5)

root.config(bg="PaleVioletRed3")
root.update()
time.sleep(1.5)

root.config(bg="MediumPurple1")
root.update()
time.sleep(1.5)

root.config(bg="MediumPurple2")
root.update()
time.sleep(1.5)

root.config(bg="MediumPurple3")
root.update()
time.sleep(1.5)

root.config(bg="black")
root.update()

time.sleep(3)

root.iconify()

root.mainloop()
