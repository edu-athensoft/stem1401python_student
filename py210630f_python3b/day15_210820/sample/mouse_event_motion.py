"""
mouse event
<Motion>

Move mouse and display current coordinate at the bottom

"""


from tkinter import *


def handler(event):
    print(f'current position is at ({event.x}, {event.y})')

    x = event.x
    y = event.y

    textvar = "Mouse position is  x:{}, y:{}".format(x,y)
    var.set(textvar)



root = Tk()
root.title("Event Handling")
root.geometry("640x480+300+300")
root.config(bg="#ddddff")

# init position of mouse cursor
x = 0
y = 0

# label of text (x,y)

var = StringVar()
text = "Mouse position is  x:{}, y:{}".format(x,y)

var.set(text)

label_coord = Label(root, textvariable= var)
label_coord.pack(anchor=S, side=RIGHT, padx=10, pady=10)

# test mouse motion
root.bind('<Motion>', handler)

root.mainloop()