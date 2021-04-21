"""
Homework 12
"""
"""
solution
of homework 2021-Mar-27
assuming that the numbers have been set from the keyboard and stored in a list
key points:
command=lambda num=i:response(num)
lambda function may accept parameter 'num'
each time you have to pass an argument(with a value) to lambda function as 'num'
then you will get one lambda with specific 'num' at each clicking
P.S.
You may or may not use inner function which is introduced in last class for this problem
Instead, I simplified that and you may easily follow and evaluate.
"""

from tkinter import *

def response(num):
    label1 = Label(root, text=str(numbers[num]))
    label1.pack()
    # print(num)

root = Tk()
root.title('Python GUI - Button')
root.geometry('640x480+300+300')
root.config(bg='#ddddff')


numbers = [1, 3, 5, 9, 11]

for i in range(len(numbers)):
    btn_1 = Button(root, text=str(numbers[i]), padx=5, pady=5,
            command=lambda num=i:response(num))\
            .pack(anchor=S, side=LEFT, ipadx=5, ipady=5)

btn_2 = Button(root, text="Exit", padx=5, pady=5,
            command=root.destroy)\
            .pack(anchor=S, side=RIGHT, ipadx=5, ipady=5)

root.mainloop()