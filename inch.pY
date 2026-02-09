import tkinter as tk
from tkinter import messagebox

def convert_to_cm():
    try:
        inches = float(entry_inch.get())
        cm = inches * 2.54
        result_label.config(text=f"Length in centimeters: {cm:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("350x200")

label_inch = tk.Label(root, text="Enter length in inches:")
label_inch.pack(pady=10)

entry_inch = tk.Entry(root)
entry_inch.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_to_cm)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
