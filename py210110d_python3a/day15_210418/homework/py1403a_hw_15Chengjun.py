from tkinter import *
from tkinter import messagebox as msg


def pwd():
    title = "Login log"
    if username == account.get() and password == password.get():
        text = 'login successfully'
        msg.showinfo(title, text)
    else:
        text = 'wrong username or password'
        msg.showerror(title, text)


def showPwd():
    enter = password
    enter['show'] = ''


def hidePwd():
    enter = password
    enter['show'] = '*'


# main program
root = Tk()
root.title("Entry")
root.geometry("400x200")

username = "admin"
password = "123456"

accountL = Label(root, text="Account ")
accountL.grid(row=2, padx=(50, 5), sticky="e")

Pwd = Label(root, text="Password ")
Pwd.grid(row=3, padx=(50, 5))

account = Entry(root, width=20)
account.grid(row=2, column=1, padx=(5, 50))

password = Entry(root, show="*", width=20)
password.grid(row=3, column=1, padx=(5, 50), sticky="e")

enter_button = Button(root, text="Login", command=pwd)
enter_button.grid(row=4, columnspan=2)

showBtn = Button(root, text='+', command=showPwd)
showBtn.grid(row=3, column=2, padx=(5, 0))

showBtn = Button(root, text='×', command=hidePwd)
showBtn.grid(row=3, column=3, padx=(5, 50))

root.mainloop()
