from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Fields cannot be blank")
    else:
        # display message with data entered
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}, \nPassword: {password} \n Save?")

        if is_ok:
            #open and write inptus to a file
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{website} | {email} | {password}\n')

                #clear inputs after saving data
                website_input.delete(0, END)
                password_input.delete(0, END)

# UI Setup #

#window setup
window = Tk()      
window.title("Password manager")

#img setup
canvas = Canvas(width=200, height=200)      
canvas.pack(padx=50,pady=50)
img = PhotoImage(file="path")     
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
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

# email address input
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(INSERT, 'sebastians9876@gmail.com')

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

#buttons 

# button used for generating a password
generate_pass_button = Button(text="Generate", command=generate_pass)
generate_pass_button.grid(row=3, column=2)

# button used for submiting data
add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()