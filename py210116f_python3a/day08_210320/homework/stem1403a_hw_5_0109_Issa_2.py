"""
place and show two image label
1. png image
2. gif image
"""


from tkinter import *


root = Tk()
root.title("Python GUI - Homework images")

# 16:9
window_width = 1200
window_height = 675

# window centered
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
x = int(screenwidth/2 - window_width/2)
y = int(screenheight/2 - window_height/2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.config(bg="saddle brown")

# place an image label - png image
png1 = PhotoImage(file='./Samoyed.png')
text1 = "A .PNG image of a smiley samoyed!!!"

label1 = Label(root, width=1100, height=600,
               bg="red4",
               # fg="white",
               # font="Verdana 12 underline",
               relief="solid", image=png1)
label1.pack()
label1_txt = Label(root,
               bg="red4",
               fg="white",
               text = text1,
               font="Verdana 12 underline")
label1_txt.pack()

# place an image label - gif image
gif1 = PhotoImage(file='./GIF SAMOYED.gif')
text2="A .GIF image of a smiley samoyed!!!"

label2 = Label(root, width=1100, height=600,
               bg="red4",
               # fg="white",
               # font="Verdana 12 underline",
               relief="solid", image=gif1)
label2.pack()

root.mainloop()
