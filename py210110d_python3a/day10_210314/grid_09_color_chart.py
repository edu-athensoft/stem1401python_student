"""

"""


from tkinter import *

root = Tk()
# root.geometry('640x480+200+200')
root.geometry('+400+300')
root.config(bg='#ddddff')
root.title('Python GUI - Grid')

colors = ["red", "orange", "yellow", "green","cyan", "blue", "purple"]

r = 0

for color in colors:
    # create text label
    label_left = Label(root, text=color, relief='groove', width=20, padx=20, pady=20)
    label_left.grid(row= r,  column= 0)

    # create color label
    label_right = Label(root, bg=color, padx=80, pady=20)
    label_right.grid(row=r, column=1)

    r += 1

root.mainloop()
