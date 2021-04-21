"""
stem1403a_homework_5_0206_steven
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


label1 = tk.Label(root, bg='blue', padx = 20, pady = 10, text="mylabel1", compound = "left", bitmap="error")
label2 = tk.Label(root, bg='blue', padx = 20, pady = 10, text="mylabel2", compound = "right", bitmap="info")
label3 = tk.Label(root, bg='blue', padx = 20, pady = 10, text="mylabel3", compound = "center", bitmap="questhead")
label4 = tk.Label(root, bg='blue', padx = 20, pady = 10, text="mylabel4", compound = "bottom", bitmap="question")
label5 = tk.Label(root, bg='blue', padx = 20, pady = 10, text="mylabel5", compound = "top", bitmap="warning")


for i in range(1,6):
    obj = 'label' + str(i)
    eval(obj).pack()


root.mainloop()
