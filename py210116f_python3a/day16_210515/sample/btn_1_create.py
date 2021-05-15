"""
Button

create a button

# high order function
# callback function
"""

from tkinter import *

# Hoist
def myresponse():
    print("I was clicked!")


# main program
root = Tk()
root.geometry('640x480+200+200')
# root.geometry('+400+300')
root.config(bg='#ddddff')
root.title('Python GUI - Button')


# create a button
# btn1 = Button(root, text='Click me!', command=myresponse())
btn1 = Button(root, text='Click me!', command=myresponse)
btn1.pack(padx=20, pady=40)

# create a button for closing and to exit
btn2 = Button(root, text='Close', command=root.destroy)
btn2.pack()

root.mainloop()


