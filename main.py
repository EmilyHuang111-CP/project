import tkinter as tk
from tkinter import ttk, messagebox
from locator import *


# Data for combobox
options = active_facility_id_name()

# Function to filter combobox options based on input
def search(event):
    value = var.get()
    if value == '':
        drop['values'] = options
    else:
        data = []
        for item in options:
            if value.lower() in item.lower():
                data.append(item)
        drop['values'] = data

# Function to handle enter button click
def click():
    selected_value = int(var.get().split(" ")[0])
    facility_name_var.set(f"{match_facility_name(selected_value)}")
    institution_name_var.set(f"{match_institution_name(selected_value)}")
    institution_id_var.set(f"{match_institution_id(selected_value)}")


    # Update label2 text
    label2_text.set(f"Facility Name: {facility_name_var.get()}   Facility ID: {selected_value}   Institution Name: {institution_name_var.get()}   Institution ID: {institution_id_var.get()}")

    # Show label2
    label2.pack()

# Create main window
root = tk.Tk()
root.geometry("1000x700")
root.title("Facility Statistics")
root.resizable(False, False)

# Label
label = tk.Label(root, text="Please choose a facility:")
label.pack()

# Combobox
var = tk.StringVar()
drop = ttk.Combobox(root, textvariable=var)
drop['values'] = options
drop.pack()

# Variables for facility information
facility_name_var = tk.StringVar()
institution_name_var = tk.StringVar()
institution_id_var = tk.StringVar()

# Second Label (Initially hidden)
label2_text = tk.StringVar()
label2_text.set("")
label2 = tk.Label(root, textvariable=label2_text)

# Buttons
enter_button = tk.Button(root, text='Find', command=click)
enter_button.pack()


# Bindings
drop.bind('<KeyRelease>', search)
drop.bind('<<ComboboxSelected>>', lambda event: var.set(drop.get()))

# Start the main tkinter event loop
root.mainloop()
