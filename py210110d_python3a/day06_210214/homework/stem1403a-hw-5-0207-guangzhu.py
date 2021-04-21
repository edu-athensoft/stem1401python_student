"""
[Homework]
Date: 2021-02-07
1. Try out label widget
Description:
create a window based on previous homework
set icon, title, dimension, maxsize, minsize, bg and any other options for the window as much as you know
create at least 2 text Labels
set dimension, font, fg, bg, font and any other options you know.
create at least 2 bitmap Labels
set dimension, fg, bg, font and any other options you know.
"""
"""
score:
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
root.geometry('{}x{}+{}+{}'.format(500, 350, pos_x, pos_y))

root.config(bg='LightPink1')
root.attributes("-topmost", True)
root.maxsize(1600, 900)
root.minsize(300, 200)
root.resizable(True, 1)

# widgets
label = Label(root, text='My homework label',
              width=200, height=5,
              bg='gold', fg='purple',
              anchor=NW, wraplength=80)
label.pack()
label1 = Label(root, text='My homework label 2',
                  width=10, height=4,
                  bg='DarkOrchid1', fg='turquoise2',
                  font='Times 12 bold roman overstrike',
                  padx=50,
                  pady=30)
label1.pack()
label2 = Label(root,width=100, height=60,
                  bg='LightCyan3', fg='green',
                  bitmap='info',
                  padx=50,
                  pady=5, anchor=N)
label2.pack()
label3 = Label(root,width=60, height=60,
                  bg='LightSkyBlue4', fg='ghost white',
                  bitmap='question',
                  padx=100,
                  pady=100, anchor=SE)
label3.pack()

# root.geometry('{}x{}+{}+{}'.format(500, 350, pos_x, pos_y))
root.mainloop()