"""
Homework
"""

"""
score
perfect

"""

from tkinter import *

root = Tk()
root.title("Python GUI - Homework")

win_width = 640
win_height = 480

positionRight = int(root.winfo_screenwidth() / 2 - win_width/2 )
positionDown = int(root.winfo_screenheight() / 2 - win_height/2 )

root.maxsize(900, 600)
root.minsize(100, 70)

root.geometry(f"{win_width}x{win_height}+{positionRight}+{positionDown}")

mytext = 'MyText Label 6'
label1 = Label(root, text=mytext,
                  width=30, height=7,
                  bg='blue', fg='#ffffff',
                  anchor=N)
lable2 = Label(root,bg = 'green',bitmap = 'info', padx = 20, pady = 10)

label1.pack()
lable2.pack()

root.update()
root.configure(bg='#ffdddd')

# create a label with image in .gif
bgimg = PhotoImage(file='./img/pimon.gif')
label3 = Label(root, image=bgimg)

# center on screen
label3.pack()

root.mainloop()