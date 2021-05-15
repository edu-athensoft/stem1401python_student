"""
Radiobutton widget

Class 1. styling
activebackground
activeforeground
background
bd
bg
borderwidth
disabledforeground
fg
font
foreground
highlightbackground
highlightcolor
highlightthickness
offrelief
overrelief
relief
selectcolor
underline
wraplength

Class 2. layout
anchor
width
height
justify
padx
pady


Class 3. features (functionalities)
text
bitmap  (context)
compound
image
cursor
selectimage

command
takefocus
textvariable

value
variable

state
tristateimage
tristatevalue

Class 4. other/misc
indicatoron
"""


from tkinter import *


def printOption():
    option = var.get()
    print(option)
    txt.set(option)



root = Tk()
root.title('Python GUI - Radiobutton')
root.geometry('640x480+300+200')
root.config(bg="#ddddff")

# Radiobutton
# var = StringVar()
var = IntVar()
# var.set(None)
var.set(2)
# var.set('')  // error
radiobtn1 = Radiobutton(root, text="Mage", variable=var, value=1, command=printOption)
radiobtn1.pack()

radiobtn2 = Radiobutton(root, text="Warrior", variable=var, value=2, command=printOption)
radiobtn2.pack()

radiobtn3 = Radiobutton(root, text="Archer", variable=var, value=3, command=printOption)
radiobtn3.pack()

# use selected option
txt = StringVar()
txt.set('Please choose a role.')
label1 = Label(root, textvariable=txt, font=(None, 20))
label1.pack()

root.mainloop()
