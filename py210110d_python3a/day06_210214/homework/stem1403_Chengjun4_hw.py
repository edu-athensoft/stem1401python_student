"""

"""

"""
score:
one fatal error (-10)
bg and fg color are the same

improper file name (-1)

"""

import tkinter as tk
root = tk.Tk()
root.title('Python GUI - Homework')
winw = 800
winh = 450
posx = 300
posy = 200
root.geometry("{}x{}+{}+{}".format(winw, winh, posx, posy))
root.config(bg="gold")
root.maxsize()
root.minsize(1600, 900)
root.attributes('-topmost', True)
root.resizable(1, 1)
mytext = 'Text Label'
label1 = tk.Label(root, text=mytext,
                  width=30, height=3,
                  bg='blue', fg='#ffffff',
                  font='Helvetica 24 italic underline',
                  padx=20,
                  pady=40)
label1.pack()
label2 = tk.Label(root, text=mytext,
                  width=60, height=4,
                  bg='pink', fg='#a3a498',
                  font='Times 18 bold underline',
                  padx=30,
                  pady=90)
label2.pack()
label3 = tk.Label(root,
                  width=60, height=70,
                  bg='red', fg='#222222',
                  bitmap='error',
                  padx=50,
                  pady=90)
label3.pack()
label4 = tk.Label(root,
                  width=50, height=50,
                  bg='green', fg='#237854',
                  ### bg='blue', fg='#237854',
                  bitmap='question',
                  padx=60,
                  pady=50)
label4.pack()
root.mainloop()