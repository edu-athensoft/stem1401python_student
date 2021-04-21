"""
Homework
Date: 2021-03-27
Input N numbers from your keyboard
Put them into a list  (i.e. [1,3,5])
Create a window
Then place(add) N buttons to the window
anchor=S
side=LEFT, side=RIGHT
Button text is the current number you get
Create an 'Exit' button
which allows you to press it to close the window
Hint:
Lambda
pass parameter
only one callback function
Due date: by the end of next Friday
"""


from tkinter import *

x = list(map(int, input("Enter multiple numbers (use <space> as separator): ").split()))
print("Numbers: ", x)

root = Tk()
root.geometry("640x480+300+300")
root.title("Python Buttons")
root.config(bg="#dddfff")


for i in x:
    btn1 = Button(root, text=i, font="Helvetica 20 bold", bg="cyan", width=10, height=1, command = lambda:print(i))
    btn1.pack()

btn2 = Button(root, text="Exit", font ="Helvetica 20 bold", bg="cyan", command = root.destroy, width=10, height=1)
btn2.pack(pady=10)

root.mainloop()
