import tkinter as tk
from tkinter import ttk, messagebox

# Data for combobox
options = active_facility_id()

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
    selected_value = var.get()
    facility_name_var.set(f"{selected_value}")
    institution_name_var.set(f"{selected_value}")
    institution_id_var.set(f"{selected_value}")

    # Update label2 text
    label2_text.set(f"Facility Name: {facility_name_var.get()}   Institution Name: {institution_name_var.get()}   Institution ID: {institution_id_var.get()}")

    # Show label2
    label2.pack()

    # # Show messagebox with selected month
    # messagebox.showinfo("Selected Month", f"You selected: {selected_value}")

# Create main window
root = tk.Tk()
root.geometry("700x400")
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

# exit_button = tk.Button(root, text='Quit', command=root.destroy)
# exit_button.pack()

# Bindings
drop.bind('<KeyRelease>', search)
drop.bind('<<ComboboxSelected>>', lambda event: var.set(drop.get()))

# Start the main tkinter event loop
root.mainloop()
