from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# -------------------Password Generator---------------------#
# Password Generator Project

def pass_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # new_password = ""
    # for char in password_list:
    #     new_password += char
    new_password = "".join(password_list)
    password_box.insert(0, new_password)
    pyperclip.copy(new_password)


# -------------------Save Password---------------------#

def save():
    website = website_box.get()
    email = Email_box.get()
    password = password_box.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty! ")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading Old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # update the old with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:

                # Saving New data
                json.dump(data, data_file, indent=4)

        finally:
            website_box.delete(0, END)
            Email_box.delete(0, END)
            password_box.delete(0, END)


# ------------------------SAVE--------------------------#

def search_pass():
    website = website_box.get()
    try:
        with open("data.json") as data_read:
            data = json.load(data_read)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Search not found 404")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No detail exist for {website}")


# -----------------------UI SETUP----------------------#
window = Tk()
window.title("Password manager", )
# window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=photo)
canvas.grid(column=1, row=0)

window_label = Label(text="Website:", font=("Arial", 12, "bold"))
window_label.grid(column=0, row=1)
website_box = Entry(width=26)
website_box.grid(column=1, row=1)
search_button = Button(text="Search", command=search_pass)
search_button.grid(row=1, column=2)
website_box.focus()

Email_label = Label(text="Email/Username:", font=("Arial", 12, "bold"))
Email_label.grid(column=0, row=2)
Email_box = Entry(width=44)
Email_box.grid(column=1, row=2, columnspan=2)
Email_box.insert(0, "patel@gmail.com")

password_label = Label(text="Password:", font=("Arial", 12, "bold"))
password_label.grid(column=0, row=3)
password_box = Entry(width=26)
password_box.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=pass_generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
