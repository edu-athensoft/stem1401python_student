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

root.title("Christmas Tree")

root.iconbitmap("./Tree.ico")

window_width = 1200
window_height = 600

screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()

x = int(screenwidth/2 - window_width/2)
y = int(screenheight/2 - window_height/2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.maxsize(1600, 900)

root.minsize(320, 180)

root.resizable(1, 1)

my_label = tk.Label(root, text="Please do not close this window before it becomes black!", width=100, height=3, bg="white", fg="cyan3", anchor="e", font="Gabriola 18 italic")
my_label.pack()

my_label = tk.Label(root, text="Thanks!", width=60, height=4, bg="red", fg="orange", anchor="se", font="Times 15 underline")
my_label.pack()

my_label = tk.Label(root, text="Have a wonderful day!", width=45, height=4, bg="green", fg="lime", anchor="w", font="Algerian 20 bold italic")
my_label.pack()

my_label = tk.Label(root, text="See you next time.", width=60, height=5, bg="blue", fg="yellow", anchor=tk.NW, font='"Courier New" 18 bold')
my_label.pack()

my_btn = tk.Button(root, text="Close", width=15, height=2, bg="brown", font="Harrington 15 bold overstrike", command=root.destroy)
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
