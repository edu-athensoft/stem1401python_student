"""
[Homework]
Date: 2021-02-07
1. Try out label widget
Description:
create a window based on previous homework
set icon, title, dimension, maxsize, minsize, bg and any other options for the window as much as you know
create at least 2 text Labels
set dimension, font, fg, bg, font and any other options you know.
create at least 2 bitmap Labels
set dimension, fg, bg, font and any other options you know.
"""
"""
score:
invalid char in file name (-1)

"""

import tkinter as tk

# window
root = tk.Tk()
root.title('Python GUI - Homework')

winw = 800
winh = 450
posx = 300
posy = 200
root.geometry("{}x{}+{}+{}".format(winw, winh, posx, posy))
# root.iconbitmap("IMG_2408.ico")

root.config(bg="gold")
root.maxsize()
root.minsize(1600, 900)
root.attributes('-topmost', True)
root.resizable(1, 1)

mytext = 'My Text Label'
label1 = tk.Label(root, text=mytext,
                  width=30, height=3,
                  bg='red', fg='#ffffff',
                  font='Helvetica 20 italic underline',
                  padx=20,
                  pady=40)
label1.pack()

label2 = tk.Label(root, text=mytext,
                  width=60, height=4,
                  bg='yellow', fg='#a3a498',
                  font='Times 19 bold underline',
                  padx=30,
                  pady=90)
label2.pack()

label3 = tk.Label(root,
                  width=60, height=70,
                  bg='green', fg='#222222',
                  bitmap='error',
                  padx=50,
                  pady=90)
label3.pack()

label4 = tk.Label(root,
                  width=50, height=50,
                  bg='blue', fg='#237854',
                  bitmap='questhead',
                  padx=60,
                  pady=50)
label4.pack()


root.mainloop()