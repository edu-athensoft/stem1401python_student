"""
eval()

function:
1. str -> executable expression -> calculate the value -> return

2. str -> Object
"""
from tkinter import *

expression = input('Enter your math expr: ')
print(expression)

res = eval(expression)
print(res)


#
root = Tk()
list_label = ['label1','label2','label3']

label1 = Label(root)
label2 = Label(root)
label3 = Label(root)

for labelname in list_label:
    eval(labelname).pack()
    # label2.pack()
    # label3.pack()
