"""
score
no docstring of comment (-5)

"""

import tkinter
import time
root = tkinter.Tk()
root.title("Homework, Label")
image = False
if image:
    root.iconbitmap(image)
    w_width = int(input("Please enter the desired width for your widget: "))
    w_height = int(input("Please enter the desired height for your widget: "))
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    top_left_x = int(sw / 2 - w_width / 2)
    top_left_y = int(sh / 2 - w_height / 2)
    root.geometry(f"{w_width}x{w_height}+{top_left_x}+{top_left_y}")

# root.configure(background="purple")
# root.configure(bg="purple")
root.config(bg='purple')

root.wm_attributes("-topmost", True)
root.maxsize(1600, 900)
root.minsize(300, 200)
root.resizable(1, 1)
label1 = tkinter.Label(root, text="This is a normal sized label :)", fg="pink", bg="gray", font=12, width=20, height=1)
label1.pack()
label2 = tkinter.Label(root, text="Big Label (:", fg="gold", bg="blue", font=16, width=80, height=20)
label2.pack()
label3 = tkinter.Label(root, text="tiny", fg="white", bg="black", font=5, width=2, height=1)
label3.pack()
label3 = tkinter.Label(root, text="You may resize the window (you have 10 secs), "
                                  "the new dimension will be echoed in console"
                       , fg="green", bg="pink")
label3.pack()
root.update()
time.sleep(10)
root.update()
print("Your window's width =", root.winfo_width())
print("Your window's height =", root.winfo_height())
root.mainloop()
