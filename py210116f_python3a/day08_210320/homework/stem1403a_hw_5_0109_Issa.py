"""
### docstring
place and show two image label
1. png image
2. gif image

 - PNG and GIF
"""


from tkinter import *


root = Tk()
root.title("Python GUI - Homework images")

### 16:9
window_width = 1200
window_height = 675

### window centered
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
x = int(screenwidth/2 - window_width/2)
y = int(screenheight/2 - window_height/2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.config(bg="saddle brown")

### place an image label - png image
png = PhotoImage(file='./Samoyed.png')
label1 = Label(root, text="A .PNG image of a smiley samoyed!!!", width=1100, height=600, bg="red4", fg="white", anchor="n", wraplength="90", font="Verdana 12 underline", relief="solid", image=png)
label1.pack()

### place an image label - gif image
gif = PhotoImage(file='./GIF SAMOYED.gif')
label2 = Label(root, text="A .GIF image of a smiley samoyed!!!", width=1100, height=600, bg="red4", fg="white", anchor="n", wraplength="90", font="Verdana 12 underline", relief="solid", image=gif)
label2.pack()

root.mainloop()
