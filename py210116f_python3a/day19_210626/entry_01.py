"""
Entry widget
"""


from tkinter import *

root = Tk()
root.title('Python GUI - Entry')
root.geometry("640x480+300+300")

# username
label_username = Label(root, text='Username')
entry_username = Entry(root)
label_username.grid(row=0,column=0, sticky='e', padx=(50,0))
entry_username.grid(row=0,column=1)

# password
label_password = Label(root, text='Password')
entry_password = Entry(root)
label_password.grid(row=1,column=0, sticky='e',padx=(50,0))
entry_password.grid(row=1,column=1)

root.mainloop()