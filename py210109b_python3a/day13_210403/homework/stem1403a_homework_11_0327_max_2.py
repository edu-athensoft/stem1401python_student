"""
Homework 11
"""

from tkinter import *

numbers = [25, 30, 98, 3150, 93, 260, 205, 57, 10]


def response(i):
    # print("ok")
    def getlabel(x):
        Label(root, text=str(x)).pack(anchor=N)
        # label1['text'] = str(i)
        # label1.pack()
    # print(numbers[i])
    return lambda:getlabel(i)



root = Tk()
root.title('Python GUI - Button')
root.geometry('640x480+300+300')
root.config(bg='#ddddff')

buttons = []
for i in numbers:
    # print(i)
    # btn = Button(root, text=str(i), font='Helvetica 10',command=response(i))
    btn = Button(root, text=str(i), font='Helvetica 10',command=response(i))
    btn.pack(anchor=S, side=LEFT, ipadx=5, ipady=5)
    buttons.append(btn)

# for i in range(len(numbers)):
#     buttons[i].config(command=lambda: response(i))

# buttons[0].config(command=lambda: response(0))
# buttons[1].config(command=lambda: response(1))
# buttons[2].config(command=lambda: response(2))
# buttons[3].config(command=lambda: response(3))
# buttons[4].config(command=lambda: response(4))
# buttons[5].config(command=lambda: response(5))
# buttons[6].config(command=lambda: response(6))
# buttons[7].config(command=lambda: response(7))

exit_btn = Button(root, text="Exit", font='Helvetica 10', command=lambda: root.destroy())
exit_btn.pack(anchor=N, side=RIGHT, ipadx=5, ipady=5)

root.mainloop()
