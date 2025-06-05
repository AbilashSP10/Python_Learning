import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import csv
from tkinter import filedialog

conn = sqlite3.connect('admin.db')
cursor = conn.cursor() # it allows to execute the query
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        email TEXT,
        phone TEXT
        )
        ''')

root = tk.Tk()
root.title("Login/Register Example")
root.geometry("350x400")
root.configure(bg="#008080",bd=5,relief="ridge")

def clear_window():
    for i in root.winfo_children(): #it is used for remove the old content and new content will appear on the smae window
        i.destroy()

def Login():
    clear_window()

    tk.Label(root, text="Login",font=("Calibri", 25, "bold"),fg="white",bg="#008080").pack(pady=15)

    frame1=tk.Frame(root,background="#008080")
    frame1.pack(side="top")

    tk.Label(frame1,text="Username: ",font=("Calibri", 15, "bold"),fg="white", bg="#008080").pack(side=tk.LEFT,padx=2)
    Susername=tk.Entry(frame1,bd=5,relief="sunken",background="ivory",foreground="black",font=("Arial", 12))
    Susername.pack(side=tk.LEFT,pady=15)

    frame2=tk.Frame(root,background="#008080")
    frame2.pack(side="top")

    tk.Label(frame2,text="Password: ",font=("Calibri", 15, "bold"), fg="white", bg="#008080").pack(side=tk.LEFT,padx=2)
    Spassword=tk.Entry(frame2,bd=5,relief="sunken",background="ivory",foreground="black",font=("Arial", 12, "bold"),show="#")
    Spassword.pack(side=tk.LEFT,pady=30)

    frame3=tk.Frame(root,background="#008080")
    frame3.pack(side="top")

    tk.Button(frame3,text="Login",font=("Calibri", 15, "bold")).pack(side=tk.LEFT,padx=10)
    tk.Button(frame3,text="Register",font=("Calibri", 15, "bold"),command=Register).pack(side=tk.LEFT)

    Suser=Susername.get()
    Spass=Spassword.get()    
    admin_dashboard(Suser,Spass)

    


def admin_dashboard(Suser,Spass):
    if Suser=="admin" and Spass=="admin123":
        awindow = tk.Tk()
        awindow.title("Admin")
        awindow.geometry("350x400")
        awindow.configure(bg="#008080",bd=5,relief="ridge")

        tk.Label(awindow, text="Hello Admin")

    else:
        messagebox.showerror("Error", "Invalid Credentials")



def Register():
    # clear_window()

    window=tk.Tk()
    window.title("Register")
    window.geometry("350x400")
    window.configure(bg="#008080")

    tk.Label(window,text="Register", font=("Calibri", 25, "bold"), fg="white", bg="#008080").pack(side=tk.TOP)

    Rframe=tk.Frame(window,background="#008080")
    Rframe.pack(side="top")

    
    tk.Label(Rframe,text="Username: ",font=("Calibri", 15, "bold"),fg="white", bg="#008080").pack(side=tk.LEFT,padx=2)
    username=tk.Entry(Rframe,bd=5,relief="sunken",background="ivory",foreground="black",font=("Arial", 12))
    username.pack(side=tk.LEFT,pady=15)

    Rframe2=tk.Frame(window,background="#008080")
    Rframe2.pack(side="top")

    tk.Label(Rframe2,text="Password: ",font=("Calibri", 15, "bold"), fg="white", bg="#008080").pack(side=tk.LEFT,padx=2)
    password=tk.Entry(Rframe2,bd=5,relief="sunken",background="ivory",foreground="black",font=("Arial", 12, "bold"),show="#")
    password.pack(side=tk.LEFT,pady=15)

    Rframe3=tk.Frame(window,background="#008080")
    Rframe3.pack(side="top")

    tk.Label(Rframe3,text="       Email: ",font=("Calibri", 15, "bold"), fg="white", bg="#008080").pack(side=tk.LEFT,padx=2)
    email=tk.Entry(Rframe3,bd=5,relief="sunken",background="ivory",foreground="black",font=("Arial", 12, "bold"))
    email.pack(side=tk.LEFT,pady=15)

    Rframe4=tk.Frame(window,background="#008080")
    Rframe4.pack(side="top")

    tk.Label(Rframe4,text="      Phone: ",font=("Calibri", 15, "bold"), fg="white", bg="#008080").pack(side=tk.LEFT,padx=2)
    phone=tk.Entry(Rframe4,bd=5,relief="sunken",background="ivory",foreground="black",font=("Arial", 12, "bold"))
    phone.pack(side=tk.LEFT,pady=15)

    Rframe5=tk.Frame(window,background="#008080")
    Rframe5.pack(side="top")        

    


    def Register_user():

        user=username.get()
        pswd=password.get()
        eml=email.get()
        phn=phone.get()

        if user=="admin":
            messagebox.showerror("Error", "You cannot use the username admin!")

        elif not user or not pswd or not eml or not phn:
            messagebox.showerror("Error", "Field cannot be blank")

        else:
            messagebox.showinfo("Success", "Successfully Registered")
            Login()
            window.destroy()
            

    tk.Button(Rframe5,text="Register",font=("Calibri", 15, "bold"),command=Register_user).pack(side=tk.LEFT,pady=15,padx=15)  

    # clear_window()
    # window.destroy()
    # root.destroy()

Login()

root.mainloop()