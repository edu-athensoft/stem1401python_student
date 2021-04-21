"""
Button
click and response
option: command

func()  -> call a function, get the returned value

how to click and exit

"""

from tkinter import *

def yourfname():
    print("I was clicked!")


root = Tk()
root.title('Python GUI - Button')
root.geometry('640x480+300+300')
root.config(bg='#ddddff')


btn1 = Button(root, text='Click me', command=yourfname)
# btn1 = Button(root, text='Click me', command=response())
btn1.pack()


btn2 = Button(root, text='Exit', command=root.destroy)
# btn1 = Button(root, text='Click me', command=response())
btn2.pack()


root.mainloop()