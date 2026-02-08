import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please enter a password", fg="black")
    elif length < 6:
        result_label.config(text="Weak Password", fg="red")
    elif 6 <= length < 10:
        result_label.config(text="Medium Password", fg="orange")
    else:
        result_label.config(text="Strong Password", fg="green")

window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("300x200")

label = tk.Label(window, text="Enter Password:")
label.pack(pady=10)

entry = tk.Entry(window, show="*")
entry.pack(pady=5)

button = tk.Button(window, text="Check Strength", command=check_strength)
button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
