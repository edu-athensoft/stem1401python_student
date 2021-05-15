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


def printInfo1():
    print(rdbtn['text'])

def printInfo2():
    # print("I clicked.")
    print(txt.get())


root = Tk()
root.title('Python GUI - Radiobutton')
root.geometry('640x480+300+200')
root.config(bg="#ddddff")

# Radiobutton

rdbtn = Radiobutton(root, text='Warrior', command=printInfo1)
rdbtn.pack()

txt = StringVar()
txt.set('Mage')
rdbtn2 = Radiobutton(root, command=printInfo2, textvariable=txt)
rdbtn2.pack()

# list all options
# for key in rdbtn.keys():
#     print(key)

root.mainloop()
