"""
Tkinter

label relief

flat
groove
raised
ridge
solid
sunken

"""


from tkinter import *


root = Tk()
root.title('Python GUI - Label justify')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

reliefs = ['flat','groove','raised','ridge','solid','sunken']


for ref in reliefs:
    Label(root, relief=ref, text=ref, padx=30, pady=15,
               font = "Helnetic 20 bold italic",
               bg='#72AAEF', fg='black').pack()

root.mainloop()
