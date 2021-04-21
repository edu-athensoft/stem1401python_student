"""
font in a label

padx = a
pady = b


"""

import tkinter as tk
# from tkinter import *

root = tk.Tk()
root.title('Python GUI - compound label')

winw= 800
winh= 600
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='#ddff77')

# create a label
mytext = 'My Text Label bitmap'
label1 = tk.Label(root,bg='white',text="my label 1", compound='left', bitmap = 'error',padx = 20, pady= 10)
label2 = tk.Label(root,bg='white',text="my label 1", compound = 'right',bitmap = 'error',padx = 20, pady= 10)
label3 = tk.Label(root,bg='white',text="my label 1", compound = 'top',bitmap = 'error',padx = 20, pady= 10)
label4 = tk.Label(root,bg='white',text="my label 1", compound = 'bottom',bitmap = 'error',padx = 20, pady= 10)
label5 = tk.Label(root,bg='white',text="my label 1", compound = 'center',bitmap = 'error',padx = 20, pady= 10)

# display labels
for i in range(1, 6):
    obj = 'label' + str(i)
    eval(obj).pack()


# res = eval('1+2*3')
# print(res)

root.mainloop()



