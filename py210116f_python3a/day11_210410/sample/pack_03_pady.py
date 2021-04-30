"""
Layout manager:  pack()

padx, pady

"""


from tkinter import *


root = Tk()
root.title('Python GUI - Layout pack')
root.geometry('640x480+0+0')
root.config(bg='#ddddff')

label1 = Label(root, text='Python', font=('Arial', 20))
label2 = Label(root, text='Java',bg='yellow', font=('Arial', 20))
label3 = Label(root, text='Web', font=('Arial', 20))
label4 = Label(root, text='Database',bg='yellow', font=('Arial', 20))

label1.pack(side=TOP, pady=20)
label2.pack(side=TOP, pady=0)
label3.pack(side=TOP, pady=20)
label4.pack(side=TOP, pady=0)

root.mainloop()
