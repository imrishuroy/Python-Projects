import tkinter
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

my_label = Label(text="I am a level", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text"
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)

# Button


def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button got clicked")
    print(user_input.get())
    my_label.config(text=user_input.get())


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)


new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
user_input = Entry(width=10)
user_input.grid(column=3, row=2)








window.mainloop()
