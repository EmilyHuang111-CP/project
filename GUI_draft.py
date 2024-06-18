from tkinterweb import HtmlFrame
import tkinter as tk
from tkinter import ttk, messagebox
from jit import *

# Function to filter combobox options based on input
options = active_facility_id_name()
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
    facility_name_var.set(selected_value)
    institution_name_var.set(selected_value)
    institution_id_var.set(selected_value)

    # Update label2 text
    label2_text.set(f"Facility Name: {facility_name_var.get()}   Institution Name: {institution_name_var.get()}   Institution ID: {institution_id_var.get()}")

    # Show label2
    label2.pack()

    # Show messagebox with selected facility
    messagebox.showinfo("Selected Facility", f"You selected: {selected_value}")

# Create main window
root = tk.Tk()
root.geometry("1000x700")
root.title("Facility Statistics")

# Frame 1: Facility Selection
frame1 = tk.Frame(root)
frame1.pack(pady=20)

label = tk.Label(frame1, text="Please choose a facility:")
label.pack()

var = tk.StringVar()
drop = ttk.Combobox(frame1, textvariable=var)
drop['values'] = options
drop.pack()

drop.bind('<KeyRelease>', search)
drop.bind('<<ComboboxSelected>>', lambda event: var.set(drop.get()))

# Frame 2: Display Selected Facility Information
frame2 = tk.Frame(root)
frame2.pack(pady=20)

facility_name_var = tk.StringVar()
institution_name_var = tk.StringVar()
institution_id_var = tk.StringVar()
# Button
enter_button = tk.Button(frame1, text='Find', command=click)
enter_button.pack()

label2_text = tk.StringVar()
label2_text.set("")

label2 = tk.Label(frame1, textvariable=label2_text)


# HTML Browser Frame
html_frame = HtmlFrame(frame2)
html_frame.load_website("http://tkhtml.tcl.tk/tkhtml.html")
html_frame.pack(fill="both", expand=True)

# Start the main tkinter event loop
root.mainloop()
