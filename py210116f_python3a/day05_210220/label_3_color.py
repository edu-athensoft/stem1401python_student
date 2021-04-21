"""
label color
bg   background
fg   foreground - text color

"""

import tkinter as tk


root = tk.Tk()
root.title('Python GUI - Label color')

winw=800
winh=450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='#ddddff')

# create a Label
label1 = tk.Label(root, text='My Text Label 1',
                  width=40, height=7,
                  bg="yellow")
label1.pack()

# create a Label
label2 = tk.Label(root, text='My Text Label 2',
                  width=80, height=5,
                  bg="red", fg="white")
label2.pack()

# create a Label
label3 = tk.Label(root, text='My Text Label 3',
                  width=40, height=3,
                  bg="pink")
label3.pack()

# create a Label
label4 = tk.Label(root, text='My Text Label 4',
                  width=80, height=1,
                  bg="blue", fg="yellow")
label4.pack()


root.mainloop()
