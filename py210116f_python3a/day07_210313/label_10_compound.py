"""
Compound label

compound = "left","right","top","bottom","center"

"""

from tkinter import *

root = Tk()
root.title('Python GUI - Label compound')
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

myoptions = (('question','left'),
             ('info','right'),
             ('warning','top'),
             ('error','bottom'),
             ('hourglass','center'))


for option in myoptions:
    Label(root, bitmap=option[0], text=option[0],compound=option[1]).pack()

root.mainloop()
