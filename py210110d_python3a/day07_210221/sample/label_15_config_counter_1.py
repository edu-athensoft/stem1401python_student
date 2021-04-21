"""
Tkinter
Label counter

config()
after()

"""

from tkinter import *

def run_counter(digit):
    print("entered run_counter()")
    # global counter
    # counter = counter + 1
    # print("assert counter is 1",counter)
    # digit_label.config(text=str(counter))
    # digit_label.after(1000,run_counter)

    def counting():
        global counter
        counter += 1
        digit.config(text=str(counter))
        digit.after(1000, counting)
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
counter = 0
run_counter(digit_label)


root.mainloop()
