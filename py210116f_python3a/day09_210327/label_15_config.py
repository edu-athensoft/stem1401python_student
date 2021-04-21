"""
config()
after(milli-sec, function_name)
"""


from tkinter import *


def changetext():
    label1.config(text='new keys')

root = Tk()
root.title('Python GUI - keys')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')
# root.config(bg='')

# create a label widget
label1 = Label(root, text='keys',
               padx=30, pady=15,
               font="Helvetica 20",
               bg='#72EFAA', fg='black')
label1.pack()

# after 2 seconds, I change text from 'keys' to 'new keys'

label1.after(2000, changetext)

root.mainloop()