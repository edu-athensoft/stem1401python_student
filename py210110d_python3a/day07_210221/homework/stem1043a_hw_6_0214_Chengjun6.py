"""
[Homework]
Date: 2021-02-14
1. Try out label widget
Description:
create a window based on previous homework
set icon, title, dimension, maxsize, minsize, bg and any other options for the window as much as you know
create at least 2 text Labels
set dimension, font, fg, bg, font and any other options you know.
create at least 3 image Labels
one for gif, one for png, another one for jpg
set dimension, fg, bg, font and any other options you know.
Due date: by the end of next Friday
"""

"""
score:
micro defect, not clean code    (-2)
"""

import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.title("Image Labels -HW")

sw = root.winfo_screenwidth(); sh = root.winfo_screenheight()
ww = 1600; wh = 900
### micro defect, not clean code

top_left_x = int(sw/2 - ww/2); top_left_y = int(sh/2 - wh/2)
root.geometry(f"{ww}x{wh}+{top_left_x}+{top_left_y}")

root.configure(bg="gray")

root.attributes("-topmost", 1)

root.resizable(1, 1)

text_label_1 = tk.Label(root, text="Normal Label", bg="pink", fg="blue", font="times 12 underline")
text_label_2 = tk.Label(root, text="Big Label", bg="black", fg="white", font="helvetica 18 underline", padx=80, pady=30)
text_label_1.pack(), text_label_2.pack()

try:
    gif_photo = tk.PhotoImage(file="homework/cute_gif.gif")
    image_label_1 = tk.Label(root, height=200, width=400, image=gif_photo)
    image_label_1.pack()
except tk._tkinter.TclError as fe:
    print("The file <cute_gif.gif> was not found")

try:
    png_photo = tk.PhotoImage(file="homework/cute_png.png")
    image_label_2 = tk.Label(root, height=200, width=400, image=png_photo)
    image_label_2.pack()
except tk._tkinter.TclError as fe:
    print("The file <cute_png.png> was not found")

try:
    jpg_obj = Image.open("homework/llama.jpg")
    jpg_photo = ImageTk.PhotoImage(jpg_obj)
    image_label_3 = tk.Label(root, height=200, width=400, image=jpg_photo)
    image_label_3.pack()
except FileNotFoundError as fe:
    print("The file <llama.jpg> was not found")
except tk._tkinter.TclError as e:
    print(e)

root.mainloop()