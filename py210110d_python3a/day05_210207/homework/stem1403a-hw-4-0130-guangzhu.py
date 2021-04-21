"""
[Homework]
Date: 2021-01-30
1. Try out label widget
Description:
create a window based on previous homework
set icon, title, dimension, maxsize, minsize, bg and any other options for the window as much as you know
create a text Label
set dimension, font, fg, bg, font and any other options which are necessary you think.
"""

"""
score
not enough white spaces (-1)
invalid char in file name (-1)

"""

from tkinter import *
root = Tk()
root.title('python gui - homework')

# root.iconbitmap('IMG_2408.ico')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
pos_x = int(round(screen_width/2 - 500/2))
pos_y = int(round(screen_height/2 - 350/2))
root.config(bg='LightPink1')
root.attributes("-topmost", True)
root.maxsize(1600, 900)
root.minsize(300, 200)
root.resizable(True, 1)
label = Label(root, text='My homework label', width=200, height=5, bg='gold', fg='purple', anchor=NW, wraplength=80)
label.pack()
root.geometry('{}x{}+{}+{}'.format(500, 350, pos_x, pos_y))
root.mainloop()
