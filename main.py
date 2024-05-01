from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(0, random.randint(8, 10))]
    password_list += [random.choice(numbers) for _ in range(0, random.randint(2, 4))]
    password_list += [random.choice(symbols) for _ in range(0, random.randint(2, 4))]


    random.shuffle(password_list)

    password = ''.join(password_list)

    entry_p.insert(0, password)
    pyperclip.copy(password)



    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = entry_w.get()
    email = entry_eu.get()
    password = entry_p.get()



    if not password or not website:
        messagebox.showerror(title='Error message', message='Please fill in all the requested information')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered :\n '
                                                              f'Website: {website}\n'
                                                              f'Email/Username :{email}\n'
                                                              f'Password : {password}')


        if is_ok:
            with open('data.txt', 'a') as data:

                data.write(f'{website} | {email} | {password}\n')
                entry_w.delete(0, END)
                entry_p.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.configure(pady=50, padx=50)
window.title('Password Manager')

canvas = Canvas(height=200, width=200)
bild = PhotoImage(file='logo.gif')
canvas.create_image(100, 100, image=bild)
canvas.grid(row=0, column=1)

#Website
label_w = Label(text='Website:')
label_w.grid(row=1, column=0)

entry_w = Entry(width=38)
entry_w.grid(row=1, column=1, columnspan=2 )
entry_w.focus()
#Email/Username
label_eu = Label(text='Email/Username:')
label_eu.grid(row=2, column=0)

entry_eu = Entry(width=38)
entry_eu.grid(row=2, column=1, columnspan=2)
entry_eu.insert(0,'softwaretesting23@outlook.com')

#Password
label_p = Label(text='Password:')
label_p.grid(row=3, column=0)

entry_p = Entry(width=21)
entry_p.grid(row=3, column=1)


button_gp = Button(text='Generate Password', command=password_generator)
button_gp.grid(row=3, column=2)

#Add
button_add = Button(text='Add', width=36, command=save)
button_add.grid(row=4, column=1, columnspan=2)










window.mainloop()