from tkinter import *


def set_entry():
    content1 = txt.get()
    print("text at original entry = ", content1)
    txt2.set(content1)


def callbackW(*args):
    txt2.set(txt.get())


def callbackR(*args):
    print("Waring: Data is being read!")


def read():
    print("Data read:", txt.get())
    print()


root = Tk()
root.title("Python GUI - Entry")
root.geometry("360x160")

txt = StringVar()
entry = Entry(root, textvariable=txt)
entry.pack(padx=20, pady=5)
txt.trace('w', callbackW)
txt.trace('r', callbackR)

txt2 = StringVar()

entry = Entry(root, textvariable=txt)
entry.pack(padx=20, pady=5)

txt.trace('w', callbackW)
txt.trace('r', callbackR)

txt2 = StringVar()
label = Label(root, textvariable=txt2)
txt2.set("Real-time data shows here")
label.pack(padx=20, pady=5)

btn = Button(root, text="Start to Read", command=read)
btn.pack(padx=20, pady=5)
root.mainloop()
