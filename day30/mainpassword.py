from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def geberate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(8, 10) 
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    password = "#".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

#----------------------------- SEARCH ---------------------------------------#

def search():
    website = website_input.get()
    try:
        with open("day30\\data.json", "r") as search_file:
            data = json.load(search_file)
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title="Website Info", message=f"Email: {email}\nPassword: {password}")
    except:
        messagebox.showerror(title="Error", message="No Data Found")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_dict = {
        website: {
            'email': email,
            'password': password
        }
    }

    if (len(website) or len(email) or len(password)) == 0:
        messagebox.showerror(title="Error", message="Dont leave any field empty")
    else:

        result = messagebox.askokcancel(title="Details", message=f"Website: {website}\nEmail: {email}\nPassword: {password}\nAre you Ok to save?")

        if result:
            try:
                with open("day30\\data.json", "r") as data:
                    data_file = json.load(data)

                data_file.update(new_dict)
                with open("day30\\data.json", "w") as data_write:
                    json.dump(data_file, data_write, indent= 4)

            except FileNotFoundError:
                with open("day30\\data.json", "w") as data_write:
                    json.dump(new_dict, data_write, indent= 4)

            except:
                with open("day30\\data.json", "w") as data_write:
                    json.dump(new_dict, data_write, indent= 4)

            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

window.config(padx=20, pady=20)
canvas= Canvas(width=200, height=200, highlightthickness=0)
photo = PhotoImage(file="day30\\logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("Arial", 12, "bold"))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=("Arial", 12, "bold"))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Arial", 12, "bold"))
password_label.grid(column=0, row=3)

generate_button = Button(text="Generate Password", command=geberate_password)
generate_button.grid(row=3, column=2)

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2)

website_input = Entry(width=30)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "ujwalkcsps@gmail.com")

password_input = Entry(width=20)
password_input.grid(row=3, column=1)

window.mainloop()