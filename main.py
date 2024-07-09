from tkinter import *
from tkinter import messagebox
import hashlib

windows = Tk()
windows.geometry("300x250")
windows.title("Password hasher")

#finctions hesh pasword
def encryptPassword():
    password = pasword.get()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    labelH = Label(windows, text=hashed_password)
    if password != "":
        with open ('heshPass.txt', 'a') as f:
            f.write(f"{hashed_password}\n")
            messagebox.showinfo("Success", "The password has been successfully hashed into the heshPass.txt file")

        labelH.place(relx=0.5, rely=0.4, anchor=CENTER)
    else:
        messagebox.showerror("Error", "You didn't write your password")

#create object
canvas = Canvas(windows, width=250, height=250)

h1 = Label(windows, text="Enter password: ")
pasword = Entry()
btn = Button(windows, text="Encrypt", command=encryptPassword)


#draw screen object

canvas.pack()
h1.place(relx=0.5, rely=0.1, anchor=CENTER)
pasword.place(relx=0.5, rely=0.19, anchor=CENTER)
btn.place(relx=0.5, rely=0.6,  anchor=CENTER)

windows.resizable(False, False)
windows.mainloop()