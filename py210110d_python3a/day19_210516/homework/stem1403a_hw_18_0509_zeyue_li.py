"""
[Homework]
Date: 2021-05-09
Design and implement a multiple option button list on the main window.
Click on each button to show a specific toplevel window.
The number of options should be at list 5.
Due date: by the end of next Sat.
"""

from tkinter import *


def open_window(window_name):
    window = Toplevel(root)
    window.title(window_name)
    window.geometry("260x180")
    window.mainloop()


root = Tk()
root.title("Python GUI - Homework")
root.geometry("640x480")
root.config(bg="#ddddff")

buttons = ["Open window 1", "Open window 2", "Open window 3", "Open window 4", "Open window 5"]

for i in buttons:
    Button(root, text=i, command=lambda window_name=i[5:]: open_window(window_name)).pack()

root.mainloop()
