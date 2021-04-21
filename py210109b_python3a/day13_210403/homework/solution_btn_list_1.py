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
    print(num)


# main program
root = Tk()
root.title('Python GUI - Button')
root.geometry('640x480+300+300')
root.config(bg='#ddddff')

# input numbers
numbers = [11,22,33,44,55]

# create buttons
for i in range(len(numbers)):
    Button(root, text=str(numbers[i]), padx=5, pady=5,
           command=lambda num=i:response(num)).pack(anchor=S, side=LEFT, ipadx=5, ipady=5)

# create exit button
btn_exit = Button(root, text="Exit", padx=5, pady=5,
            command=root.destroy)
btn_exit.pack(anchor=S, side=RIGHT, ipadx=5, ipady=5)

root.mainloop()
