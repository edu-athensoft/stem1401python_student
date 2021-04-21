"""
keys()
get options of a widget

"""

from tkinter import *


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

# using keys()
result = label1.keys()
print(type(result))

for key in result:
    print(key)

root.mainloop()