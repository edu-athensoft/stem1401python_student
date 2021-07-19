
from tkinter import *
from tkinter import messagebox as msg

def printInfo():
    print(f"You've input: {entry1.get()} for username")
    print(f"You've input: {entry2.get()} for password")

import random
while True:
   numbers = random.randint(1000, 9999)
   print(numbers)
   if True:
       break



def numberc(numb):
    if numb == numbers:
        title = "MSG box"
        text = "Login successful"
        msg.showinfo(title, text)
    else:
        title = "MSG box"
        text = "Wrong number. Please try again."
        msg.showinfo(title, text)

def login(un, pw, rpw):
    if un == username and pw == rpw == password:
        wind = Tk()
        wind.title('Python GUI - Button')
        wind.geometry("200x200+200+200")
        wind.config(bg='#ddddff')
        label5 = Label(wind, text="Please input this number")
        label5.pack()

        label4 = Label(wind, text = numbers)
        label4.pack()

        entry4 = Entry(wind)
        entry4.pack()

        printbtn4 = Button(wind, text="SUBMIT", command=lambda: numberc(entry4.get()))
        printbtn4.pack()


        wind.mainloop()

    elif un == username and pw == password and rpw != password:
        title = "MSG box"
        text = "Your retyped password is not the same as your initial password. Please try again."
        msg.showinfo(title, text)

    else:
        title = "MSG box"
        text = "Wrong username or password. Please try again."
        msg.showinfo(title, text)

def delete():
    entry1.delete(1)
    entry2.delete(1)
    entry3.delete(1)





username = "admin"
password = "12345"

root = Tk()
root.title('Python GUI - Button')
root.geometry("320x240+200+200")
root.config(bg='#ddddff')

label1 = Label(root, text="Username")
label1.grid(row=0, column=0, padx=(50, 5))

# create Entry
entry1 = Entry(root)
entry1.grid(row=0, column=1)

label2 = Label(root, text="Password")
label2.grid(row=1, column=0, padx=(50, 5))

entry2 = Entry(root, show="*")
entry2.grid(row=1, column=1)

label3 = Label(root, text="Retype Password")
label3.grid(row=2, column=0, padx=(50, 5))

entry3 = Entry(root, show="*")
entry3.grid(row=2, column=1)

printbtn1 = Button(root, text="Print", command=lambda: login(entry1.get(), entry2.get(), entry3.get()))
printbtn1.grid(row=5, column=0,sticky = "e", pady=(5, 5))

printbtn2 = Button(root, text="Clear", command = delete)
printbtn2.grid(row=6, column=0, sticky="e", pady=(0,5))

printbtn2 = Button(root, text="Quit", command = root.destroy)
printbtn2.grid(row=7, column=0, sticky="e")

root.mainloop()