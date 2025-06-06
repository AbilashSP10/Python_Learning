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

    

    def dashboard():

        Suser=Susername.get()
        Spass=Spassword.get()
        
        clear_window()

        if Suser=="admin" and Spass=="admin123":       

            root.title("Admin Window")

            framec = tk.Frame(root, bg="#008080", bd=2, relief="groove")
            framec.pack(fill="both", expand=True, padx=10, pady=10)

            tk.Label(framec, text="Hello Admin",font=("Calibri", 25, "bold"),fg="white",bg="#008080").pack(pady=15)            

            tree = ttk.Treeview(framec, columns=("ID", "Username", "Email", "Phone"), show="headings")
            tree.heading("ID", text="ID")
            tree.heading("Username", text="Username")
            tree.heading("Email", text="Email")
            tree.heading("Phone", text="Phone")

            tree.column("ID", width=50, anchor="center")
            tree.column("Username", width=100, anchor="center")
            tree.column("Email", width=150, anchor="center")
            tree.column("Phone", width=100, anchor="center")

            tree.pack(pady=10, padx=10, fill="both", expand=True)

            cursor.execute("SELECT id, username, email, phone FROM users")
            users =cursor.fetchall()

            for user in users:
                tree.insert("", "end", values=user)

            btn_frame = tk.Frame(framec, bg="#008080")
            btn_frame.pack(pady=10)

            def view_user_details():
                selected_item = tree.focus()

                if not selected_item:
                    messagebox.showwarning("Warning", "Please select a user first.")

                else:
                    user_data = tree.item(selected_item)['values']
                    user_id = user_data[0]
                    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))

                    user = cursor.fetchone()
                    show_user_details(user)

            def delete_user():
                selected_item = tree.focus()
                user_data = tree.item(selected_item)['values']

                if not selected_item:
                    messagebox.showwarning("Warning", "Please select a user first.")

                elif user_data[1] == "admin":
                    messagebox.showerror("Error", "Cannot delete admin account.")

                else:
                    messagebox.askyesno("Confirm", f"Delete user {user_data[1]}?")
                    cursor.execute("DELETE FROM users WHERE ID=?", (user_data[0],))
                    conn.commit()
                    tree.delet(selected_item)
                    messagebox.showinfo("Success", "User deleted successfully.")

        elif cursor.execute("SELECT username, email, phone FROM users WHERE username = ? AND password = ?", (Suser,Spass)):
            user1=cursor.fetchone()

            if user1:            
                root.title(f"Hi {Suser} Welcome!!!")

                username, email, phone = user1

                framen=tk.Frame(root,background="#008080")
                framen.pack(side="top")

                tk.Label(framen,text=f"Username: {username}",font=("Calibri", 15, "bold"),fg="white",bg="#008080").pack(pady=10,side=tk.TOP)                                 
                tk.Label(framen,text=f"Email: {email}",font=("Calibri", 15, "bold"),fg="white",bg="#008080").pack(pady=10,side=tk.TOP)
                tk.Label(framen,text=f"Phone: {phone}",font=("Calibri", 15, "bold"),fg="white",bg="#008080").pack(pady=10,side=tk.TOP)

        else:            
            messagebox.showerror("Error", "Invalid Credentials")

    tk.Button(frame3,text="Login",font=("Calibri", 15, "bold"),command=dashboard).pack(side=tk.LEFT,padx=10)
    tk.Button(frame3,text="Register",font=("Calibri", 15, "bold"),command=Register).pack(side=tk.LEFT)

        
    # admin_dashboard(Suser,Spass)

    


    



def Register():          

    # window=tk.Tk()
    # window.title("Register")
    # window.geometry("350x400")
    # window.configure(bg="#008080")

    clear_window()

    root.title("Register Window")

    tk.Label(root,text="Register", font=("Calibri", 25, "bold"), fg="white", bg="#008080").pack(side=tk.TOP)

    Rframe=tk.Frame(root,background="#008080")
    Rframe.pack(side="top")

    
    tk.Label(Rframe,text="Username: ",font=("Calibri", 15, "bold"),fg="white", bg="#008080").pack(side=tk.LEFT,padx=2)
    username1=tk.Entry(Rframe,bd=5,relief="sunken",background="ivory",foreground="black",font=("Arial", 12))
    username1.pack(side=tk.LEFT,pady=15)

    Rframe2=tk.Frame(root,background="#008080")
    Rframe2.pack(side="top")

    tk.Label(Rframe2,text="Password: ",font=("Calibri", 15, "bold"), fg="white", bg="#008080").pack(side=tk.LEFT,padx=2)
    password1=tk.Entry(Rframe2,bd=5,relief="sunken",background="ivory",foreground="black",font=("Arial", 12, "bold"),show="#")
    password1.pack(side=tk.LEFT,pady=15)

    Rframe3=tk.Frame(root,background="#008080")
    Rframe3.pack(side="top")

    tk.Label(Rframe3,text="       Email: ",font=("Calibri", 15, "bold"), fg="white", bg="#008080").pack(side=tk.LEFT,padx=2)
    email1=tk.Entry(Rframe3,bd=5,relief="sunken",background="ivory",foreground="black",font=("Arial", 12, "bold"))
    email1.pack(side=tk.LEFT,pady=15)

    Rframe4=tk.Frame(root,background="#008080")
    Rframe4.pack(side="top")

    tk.Label(Rframe4,text="      Phone: ",font=("Calibri", 15, "bold"), fg="white", bg="#008080").pack(side=tk.LEFT,padx=2)
    phone1=tk.Entry(Rframe4,bd=5,relief="sunken",background="ivory",foreground="black",font=("Arial", 12, "bold"))
    phone1.pack(side=tk.LEFT,pady=15)

    Rframe5=tk.Frame(root,background="#008080")
    Rframe5.pack(side="top")

    

    # window.destroy()          

    


    def Register_user():

        # clear_window()

        user=username1.get()
        pswd=password1.get()
        eml=email1.get()
        phn=phone1.get()

        
        if user=="admin":
            messagebox.showerror("Error", "You cannot use the username admin!\n Please register again \U0001F621")
            return

        elif not user or not pswd or not eml or not phn:
            messagebox.showerror("Error", "Field cannot be blank")
            return

        else:
            try:
                cursor.execute(
                    "INSERT INTO users (username, password, email, phone) VALUES (?, ?, ?, ?)",
                    (username1.get(), password1.get(), email1.get(), phone1.get())
                )
                conn.commit()
                messagebox.showinfo("Success", "Successfully Registered")
                Login()

            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already exists!!!")            
            # clear_window()
            # window.destroy()               

    
        Login()
    

    tk.Button(Rframe5,text="Register",font=("Calibri", 15, "bold"),command=Register_user).pack(side=tk.LEFT,pady=15,padx=15)  

    # clear_window()
    # window.destroy()
    # root.destroy()

Login()

root.mainloop()