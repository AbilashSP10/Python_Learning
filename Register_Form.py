import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import csv
from tkinter import filedialog

# # pip install mysql-connector-python

# import mysql.connector
# from mysql.connector import Error

# # ...existing code ....

# try:
#     conn = mysql.connector.connect(
#         host='localhost',
#         user='root',  # default XAMPP/WAMP user
#         password='', # default is empty for XAMPP/WAMP
#         database='admin' # make sure this DB exists in phpMyAdmin        
#     )
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users(
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             username VARCHAR(255) UNIQUE NOT NULL,
#             password VARCHAR(255) NOT NULL,
#             email VARCHAR(255),
#             phone VARCHAR(20)
#         )
                   
#     ''')

# except Error as e:
#     print(f"Error connecting to MySQL: {e}")
#     exit(1)

# #.... existing code



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

    root.title("Login/Register Example")

    root.geometry("350x300")

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

    def show_user_details(user):
        if user:
            detail_window = tk.Toplevel(root)
            detail_window.title("User Details")
            detail_window.geometry("300x200")
            detail_window.configure(bg="#008080")

            labels = ["User_ID", "Username", "Password", "Email", "Phone"]
            for i, value in enumerate(user):
                # if labels[i] =="ID":
                #     value=""
                if labels[i] == "Password":
                    value = "********"
                tk.Label(detail_window, text=f"{labels[i]}: {value}", font=("Calibri", 12, "bold"), fg="white", bg="#008080").pack(pady=5)
        else:
            messagebox.showerror("Error", "Could not retrieve user details.")


    def export_to_csv():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Save user data as",
            initialfile="users.csv"
        )

        if file_path:
            cursor.execute("SELECT * From users")
            users = cursor.fetchall()
            with open(file_path, 'w', newline='') as file:
                writer=csv.writer(file)
                writer.writerow(["ID", "Username", "Password", "Email", "Phone"])
                writer.writerows(users)
            messagebox.showinfo("Sucess", f"User data exported to {file_path}")


    def dashboard():

        Suser=Susername.get()
        Spass=Spassword.get()
        
        clear_window()

        if Suser=="admin" and Spass=="admin123":       

            root.title("Admin Window")

            root.geometry("550x500")            

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
                    return

                if user_data[1] == "admin":
                    messagebox.showerror("Error", "Cannot delete admin account.")
                    return
                
                confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete user '{user_data[1]}'?")
                if confirm:
                    cursor.execute("DELETE FROM users WHERE ID=?", (user_data[0],))
                    conn.commit()
                    tree.delete(selected_item)
                    messagebox.showinfo("Success", f"User '{user_data[1]}' deleted successfully.")

                # else:
                #     messagebox.askyesno("Confirm", f"Delete user {user_data[1]}?")
                #     cursor.execute("DELETE FROM users WHERE ID=?", (user_data[0],))
                #     conn.commit()
                #     tree.delete(selected_item)
                #     messagebox.showinfo("Success", "User deleted successfully.")
            btn_frame = tk.Frame(framec, bg="#008080")
            btn_frame.pack(side="top")

            tk.Button(btn_frame, text="Delete User", font=("Calibri", 12, "bold"), bg="green", fg="white", command=delete_user).pack(side=tk.LEFT, padx=10)
            tk.Button(btn_frame, text="View Details", font=("Calibri", 12, "bold"), bg="blue", fg="white", command=view_user_details).pack(side=tk.LEFT, padx=10)
            tk.Button(btn_frame, text="Save CSV", font=("Calibri", 12, "bold"), bg="white", fg="black", command=export_to_csv).pack(side=tk.LEFT, padx=10)
            tk.Button(btn_frame, text="Logout", font=("Calibri", 12, "bold"), bg="red", fg="white", command=Login).pack(side=tk.LEFT, padx=10)
            
        else:
            cursor.execute("SELECT username, email, phone FROM users WHERE username = ? AND password = ?", (Suser,Spass))
            user1=cursor.fetchone()

            if user1:            
                root.title(f"Hi {Suser} Welcome!!!")

                username, email, phone = user1

                framen=tk.Frame(root,background="#008080")
                framen.pack(side="top")

                tk.Label(framen,text=f"Username: {username}",font=("Calibri", 15, "bold"),fg="white",bg="#008080").pack(pady=10,side=tk.TOP)                                 
                tk.Label(framen,text=f"Email: {email}",font=("Calibri", 15, "bold"),fg="white",bg="#008080").pack(pady=10,side=tk.TOP)
                tk.Label(framen,text=f"Phone: {phone}",font=("Calibri", 15, "bold"),fg="white",bg="#008080").pack(pady=10,side=tk.TOP)

                btn_frame = tk.Frame(framen, bg="#008080")
                btn_frame.pack(side="top")

                tk.Button(btn_frame, text="Logout", font=("Calibri", 12, "bold"), bg="red", fg="white", command=Login).pack(side=tk.LEFT, padx=10) 

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
    root.geometry("350x400")

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