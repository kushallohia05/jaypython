import tkinter as tk
from tkinter import ttk, messagebox

class Restaurant:
    def __init__(self, root):
        self.root=root
        self.root.title("Restaurant Order App")

        self.menu_items={"FRIES MEAL": 200, "BURGER MEAL": 300, "PIZZA MEAL": 300}

        ttk.Label(
            frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, columnspan=3, padx=10, pady=10)
        
        self.menu_labels={}
        self.menu_quantites={}

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial", 12)
            )
            label.grid(row=i, padx=10, pady=5)
            self.menu_labels[item] = label
            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry