"""
[Homework]
Date: 2021-02-14
1. Try out label widget
Description:
create a window based on previous homework
set icon, title, dimension, maxsize, minsize, bg and any other options for the window as much as you know
create at least 2 text Labels
set dimension, font, fg, bg, font and any other options you know.
create at least 3 image Labels
one for gif, one for png, another one for jpg
set dimension, fg, bg, font and any other options you know.
"""

"""
score:
invalid char in file name (-1)

"""

from tkinter import *
from PIL import Image,ImageTk
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
label = Label(root, text='My homework label',
              width=20, height=2,
              bg='gold', fg='purple',
              anchor=NW, wraplength=400)
label.pack()
label1 = Label(root, text='My homework label 2',
                  width=10, height=2,
                  bg='DarkOrchid1', fg='turquoise2',
                  font='Times 12 bold roman overstrike',
                  padx=60,
                  pady=1)
label1.pack()
image1 = PhotoImage(file='img/pimon.gif')
label2 = Label(root,width=100, height=60,
                  image=image1, bg='gold', fg='lightcyan1', padx=10, pady=5)
label2.pack()
image2 = PhotoImage(file='img/diona.png')
label3 = Label(root,width=60, height=60,
               image=image2,bg='LightSkyBlue4', fg='ghost white')
label3.pack()
image3 = Image.open('./img/dog2.jpg')
image_3_bg = ImageTk.PhotoImage(image3)
label4 = Label(root,width=200, height=60,
               image=image_3_bg,bg='LightSkyBlue2', fg='purple')
label3.pack()
root.geometry('{}x{}+{}+{}'.format(500, 350, pos_x, pos_y))
root.mainloop()