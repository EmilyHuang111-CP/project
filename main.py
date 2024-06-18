# Import necessary modules
from tkinterweb import HtmlFrame  # Assuming tkinterweb is imported correctly
import tkinter as tk
from tkinter import ttk, messagebox
from locator import *

# Function to retrieve active facility IDs and names
options = active_facility_id_name()

# Function to filter combobox options based on input
def search(event):
    value = var.get()
    if value == '':
        drop['values'] = options  # Reset options if search input is empty
    else:
        data = []
        for item in options:
            if value.lower() in item.lower():
                data.append(item)
        drop['values'] = data  # Set filtered options based on search input

# Function to handle 'Find' button click
def click():
    label2_text.set("")
    sv = var.get().strip()
    selected_value = int(sv.split(" ")[0])
    try:
        facility_name_var.set(f"{match_facility_name(selected_value)}")
        institution_name_var.set(f"{match_institution_name(selected_value)}")
        institution_id_var.set(f"{match_institution_id(selected_value)}")


        # Update label2 text
        label2_text.set(f"Facility Name: {facility_name_var.get()}   Facility ID: {selected_value}   Institution Name: {institution_name_var.get()}   Institution ID: {institution_id_var.get()}")

        # Show label2
        label2.pack()
    except:
        messagebox.showwarning("Entry not found", f"{sv} is not available as a facility.")


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
drop['values'] = options  # Set initial options in combobox
drop.pack()

drop.bind('<KeyRelease>', search)  # Bind KeyRelease event to search function
drop.bind('<<ComboboxSelected>>', lambda event: var.set(drop.get()))  # Set selected value on selection

# Frame 2: Display Selected Facility Information
frame2 = tk.Frame(root)
frame2.pack(pady=20)

facility_name_var = tk.StringVar()
institution_name_var = tk.StringVar()
institution_id_var = tk.StringVar()

# 'Find' Button
enter_button = tk.Button(frame1, text='Find', command=click)
enter_button.pack()

label2_text = tk.StringVar()
label2_text.set("")  # Initialize label2 text

label2 = tk.Label(frame1, textvariable=label2_text)

# HTML Browser Frame
html_frame = HtmlFrame(frame2)
html_frame.load_website("http://tkhtml.tcl.tk/tkhtml.html")  # Load a sample website
html_frame.pack(fill="both", expand=True)

# Start the main tkinter event loop
root.mainloop()
