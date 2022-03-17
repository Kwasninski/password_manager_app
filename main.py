from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from cv2 import meanShift
import pyperclip
import json

# Password generator
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    pw_symbols = [choice(symbols) for _ in range(randint(2,4))]

    pw_list = pw_letters + pw_numbers + pw_symbols
    shuffle(pw_list)
    password = "".join(pw_list)

    #clear password input
    password_input.delete(0, END)

    #input generated password into the field
    password_input.insert(INSERT, password)

    #copy generated password to the clipboard for easy access
    pyperclip.copy(str(password))

# Save Password #

#save passowrd function
def save_password():

    #get data from inputs
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website:{
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Fields cannot be blank")
    else:
        try:
            #open and write inptus to a file
            with open('data.json', "r") as data_file:
                # read old data
                data = json.load(data_file)
            #catch error if file doesnt exist
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                #write new data
                json.dump(new_data, data_file, indent=4)
        else:     
            #updating old data with new data
            data.update(new_data)
            #write new data to the existing file
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            #clear inputs after saving data
            website_input.delete(0, END)
            password_input.delete(0, END)


# find website password

def search_password():
    #get data from input
    website = website_input.get()
    try:
    #open data file
        with open('data.json')as data_file:
            data = json.load(data_file)
            if website in data:
                #extract "email" value from data file
                email = data[website]["email"]
                #extract "passwrd" value from data file
                password = data[website]["password"]
                #display info message with the data from the data.json file IF it exists
                messagebox.showinfo(title="Search result", message=f"email: {email} \npassword: a{password}")
            else:
                #display error message for non existing query
                messagebox.showinfo(title="Error", message="no results found")
        website_input.focus()
    # catch error exception if file has not been created 
    except FileNotFoundError:
        #display erorr message with instructions
        messagebox.showinfo(title="Error", message="No data available, add the password first")


# UI Setup #

#window setup
window = Tk()      
window.title("Password manager")

#img setup
canvas = Canvas(width=200, height=200)      
canvas.pack(padx=50,pady=50)
img = PhotoImage(file="password.png")     
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)


#labels

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username')
email_label.grid(row=2, column=0)

password_label = Label(text='Password')
password_label.grid(row=3, column=0)

##inputs

# website address input
website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

# email address input
email_input = Entry(width=38)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(INSERT, 'sebastians9876@gmail.com')

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

#buttons 

#search website password button
search_button = Button(text="Search", width=13, command=search_password)
search_button.grid(row=1, column=2, columnspan=2)

# button used for generating a password
generate_pass_button = Button(text="Generate password", command=generate_pass)
generate_pass_button.grid(row=3, column=2)

# button used for submiting data
add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()