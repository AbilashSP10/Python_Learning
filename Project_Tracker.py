import tkinter as tk

window = tk.Tk()

window.title("Project Tracker")
window.geometry("450x650")
window.configure(background="#eab676")

frm1 = tk.Frame(window,background="#eab676")
frm1.pack(side="top")

Login=tk.Button(frm1,text="Login")
Login.pack(side=tk.LEFT,pady=10,padx=5)

Register=tk.Button(frm1,text="Register")
Register.pack(side=tk.LEFT)

window.mainloop()