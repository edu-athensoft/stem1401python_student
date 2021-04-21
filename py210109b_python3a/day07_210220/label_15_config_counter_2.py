"""
Tkinter
Label counter

config()
after()

"""

from tkinter import *

def run_counter(digit):
    print("entered run_counter()")

    counter = 0

    def counting():
        nonlocal counter
        counter += 1
        digit.config(text=str(counter))
        digit.after(1000, counting)

    # def fun2():
    #     nonlocal counter
    #     counter += 2

    counting()



# main program
root = Tk()
root.title('Python GUI - Label counter')
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# label object
digit_label = Label(root,
              bg = "seagreen",
              fg = 'white',
              height = 3,
              width = 10,
              font = "Helvetic 30 bold")
digit_label.pack()


# starting count
# counter = 0
run_counter(digit_label)


root.mainloop()
