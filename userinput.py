import tkinter as tk

def show_input():
    user_input = entry.get()
    result_label.config(text="You entered: " + user_input)

root = tk.Tk()
root.title("Display Input Example")

# Entry widget (input field)
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Button to submit input
submit_button = tk.Button(root, text="Submit", command=show_input)
submit_button.pack()

# Label to display the result
result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=10)

root.mainloop()