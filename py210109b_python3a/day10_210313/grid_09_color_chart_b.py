"""
Tkinter

using grid layout

color charts
"""


from tkinter import *


root = Tk()
# root.geometry('640x480+200+200')
root.geometry('+400+300')
root.config(bg='#ddddff')
root.title('Python GUI - Grid')

colors = ["red", "orange", "yellow", "green","cyan", "blue", "purple"]

# initial row number
# r = 0

for index in range(len(colors)):
    # create text label
    Label(root, text = colors[index],
          relief="groove", width = 20, padx=20, pady=20,
          font="20").grid(row=index, column=0)

    # create no-text label
    Label(root, bg = colors[index],
          relief="flat", width = 20, padx=20, pady=20).grid(row=index, column=1)

    # r += 1

root.mainloop()
