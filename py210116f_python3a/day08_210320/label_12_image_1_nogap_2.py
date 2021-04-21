"""
Tkinter
place a label widget
image label with .jpg
does not work
"""


from tkinter import *


root = Tk()

root.title('Python GUI - Label image')

# root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label with image in .jpg
bgimg = PhotoImage(file='./img/dog2.jpg')
label1 = Label(root, image=bgimg)
label1.pack()


root.mainloop()
