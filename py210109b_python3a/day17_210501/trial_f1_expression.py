"""
feature 01.
User can input an arithmetic expression.

how to input
  user clicks buttons one by one
  desc:
     and each button generates a char
     digits: 0 - 9
     Create 10 Button objects for digit 0 - 9

how to process
  desc:
    then user get a sequence of char
    combine them into a string of expression

how to output
  step 1. list all possible solution
  opt 1. Label
  opt 2. Entry
  opt 3. Message
  opt 4. Button

  step 2. make decision
  decision:  using Label
"""

from tkinter import *


def printChar(char):
    # print("printNum", num)
    global expr
    expr += char
    print(expr)
    # return

root = Tk()
root.title("feature 01")
root.geometry("640x480")
root.config(bg="#ddddff")

expr = ''

btn1 = Button(root, text='Char 1', command=lambda: printChar('1')).pack()
btn2 = Button(root, text='Char 2', command=lambda: printChar('2')).pack()
btn3 = Button(root, text='Char 3', command=lambda: printChar('3')).pack()
btna = Button(root, text='Char +', command=lambda: printChar('+')).pack()
btnb = Button(root, text='Char -', command=lambda: printChar('-')).pack()
btnc = Button(root, text='Char %', command=lambda: printChar('%')).pack()

resultLabel = Label(root, text='\n0', width=20)
resultLabel.pack()

root.mainloop()
