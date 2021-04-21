"""
place and show two image label (.jpg)

"""
from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Python GUI - Lamborghini")
root.iconbitmap("./lambo.ico")

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


# scrollbar (doesn't work)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config()

# place an image label - png image
# create a label with image in .jpg
my_jpg_1 = Image.open("./reventon 2.jpg")
my_jpg_1 = my_jpg_1.resize((200, 150), Image.ANTIALIAS)
jpg_1 = ImageTk.PhotoImage(my_jpg_1)
label1 = Label(root, width=250, height=200,
               bg="purple3",
               relief="solid", image=jpg_1)
label1.pack()

# text for image1
text1 = "Lamborghini Reventon 1"
label1_txt = Label(root,
               bg="green3",
               fg="white",
               text=text1,
               font="Verdana 12 underline")
label1_txt.pack()


# place an image label jpg image
my_jpg_2 = Image.open("./reventon 3.jpg")
my_jpg_2 = my_jpg_2.resize((200, 150), Image.ANTIALIAS)
jpg_2 = ImageTk.PhotoImage(my_jpg_2)
label2 = Label(root, width=250, height=200,
               bg="blue3",
               relief="groove", image=jpg_2)
label2.pack()

# text2 for image 2
text2 = "Lamborghini Reventon 2"
label2_txt = Label(root,
               bg="red3",
               fg="white",
               text=text2,
               font="Verdana 12 underline")
label2_txt.pack()


# bitmap labels
label_3 = Label(root, bg="yellow3", bitmap="error", padx=20, pady=10, fg="blue", relief="sunken")
label_3.pack()

label_3_text = Label(root, bg="yellow3", text="Error", padx=20, pady=10, fg="blue")
label_3_text.pack()

label_4 = Label(root, bg="orange3", bitmap="warning", padx=20, pady=10, fg="blue", relief="ridge")
label_4.pack()

label_4_text = Label(root, bg="orange3", text="Warning", padx=20, pady=10, fg="blue")
label_4_text.pack()

root.mainloop()
