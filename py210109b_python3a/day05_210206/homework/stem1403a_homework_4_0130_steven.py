"""
stem1403a_homework_4_0130_steven
"""

"""
score
perfect

"""

import tkinter as tk
root = tk.Tk()

root.title("Python GUI - Title")

# root.iconbitmap('')
windw = 800
windh = 450

x = int(root.winfo_screenwidth()/2 - 800/2)
y = int(root.winfo_screenheight()/2 - 450/2)
root.geometry("{}x{}+{}+{}".format(800,450,x,y))
root.configure(bg='cyan')
root.attributes('-topmost',1)
root.resizable(False, False)
root.update()
print(f"The window has a height of {root.winfo_height()} and a width of {root.winfo_width()}")
root.config(bg='#ddff77')

label1 = tk.Label(root, text='Text label',
                  width=30, height=7,
                  bg='red', fg='black',
                  anchor='n')
label1.pack()

label2 = tk.Label(root, text='Text label2',
                  width=30, height=7,
                  bg='blue', fg='cyan',
                  anchor='n')
label2.pack()

root.mainloop()