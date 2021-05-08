from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

# password_list = []
#
# for char in range(nr_letters):
#     password_list.append(random.choice(letters))
#

letters_list = [random.choice(letters) for _ in range(nr_letters)]

symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]

numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]

password_list = letters_list + symbols_list + numbers_list

random.shuffle(password_list)

print(password_list)

# password = ""
# for char in password_list:
#     password += char

password = "".join(password_list)


# print(f"Your password is: {password}")

def automate_password():
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    entered_password = password_entry.get()
    email = email_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(entered_password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any of fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"Password: {entered_password}\n Click Ok to save.")

        if is_ok:
            try:
                with open("passwords.json", mode="r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                # Creating new data file
                with open("passwords.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating the old data
                data.update(new_data)
                # Updating the updating data to the file
                with open("passwords.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_input.get()
    try:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No data file found")
    else:
        if website in data:
            messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]['email']}\n Password: "
                                                            f"{data[website]['password']}")
        else:
            messagebox.showinfo(title="Oops", message=f"The {website} website entry is not found")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, )

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=2)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=3)

website_input = Entry(width=21)
website_input.grid(column=2, row=3)
website_input.focus()

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=4)

email_entry = Entry(width=35)
email_entry.insert(0, "rishu@gmail.com")
email_entry.grid(column=2, row=4, columnspan=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=5)

password_entry = Entry(width=21)
password_entry.grid(column=2, row=5)

generate_password_button = Button(text="Generate Password", command=automate_password)
generate_password_button.grid(column=3, row=5)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=2, row=6, columnspan=3)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=3, row=3)
window.mainloop()
