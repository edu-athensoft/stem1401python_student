"""
create a window
then create two frames
each of them takes half of the area of the window
one bg="color1"
the other bg="color2"

up and bottom

"""

from tkinter import *

root = Tk()
root.title("Python GUI - Frame")
root.geometry("640x480")
root.config(bg="#ddddff")

frame1 = Frame(root, bg="red",height=240)
frame1.pack(fill=BOTH)


# Label(frame1, text='Label1', bg='white').pack(pady=(0,50))
# Label(frame1, text='Label2', bg='white').pack(pady=(50,0), side=BOTTOM)

Label(frame1, text='Label1', bg='white').place(x=50, y=50)
Label(frame1, text='Label2', bg='white').place(relx=0.3, rely=0.5)

frame2 = Frame(root,bg="blue",height=240)
frame2.pack(fill=BOTH,expand=True)
# frame2.pack(relheight=0.5, relwidth=1, rely=0.5)

Label(frame2, text='Label3', bg='white').grid(row=0,column=0)
Label(frame2, text='Label4', bg='white').grid(row=1,column=1)


root.mainloop()