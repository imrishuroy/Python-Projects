from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=100, pady=50)

user_input = Entry(width=10)
user_input.grid(column=3, row=2)

miles_level = Label(text="Miles")
miles_level.grid(column=4, row=2)

equal_to_level = Label(text="is equal to")
equal_to_level.grid(column=2, row=3)

result_level = Label(text="0", font=("Arial", 24, "bold"))
result_level.grid(column=3, row=3)

km_level = Label(text="Km")
km_level.grid(column=4, row=3)


def calculate():
    miles = float(user_input.get())
    km = int(miles * 1.60934)
    result_level.config(text=f"{km}")


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=3, row=4)

window.mainloop()
