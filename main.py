import tkinter as tk
from tkinter import ttk, messagebox
from locator import active_facility_id_name, match_facility_name, match_institution_name, match_institution_id
from plotly_graph import *
import webbrowser

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
        messagebox.showwarning("Entry not found", f"{selected_value} is not available as a facility.")





# Create main window
root = tk.Tk()
root.geometry("1000x1000")
root.title("Facility Statistics")

# Retrieve active facility IDs and names
options = active_facility_id_name()

# Frame 1: Facility Selection
frame1 = tk.Frame(root)
frame1.pack(pady=20)

label = tk.Label(frame1, text="Please type in the facility id (numerical digits only):")
label.pack()

var = tk.StringVar()
drop = ttk.Combobox(frame1, textvariable=var)
drop['values'] = options  # Set initial options in combobox
drop.pack()

drop.bind('<KeyRelease>', search)  # Bind KeyRelease event to search function
drop.bind('<<ComboboxSelected>>', lambda event: var.set(drop.get()))  # Set selected value on selection

# 'Find' Button
enter_button = tk.Button(frame1, text='Find', command=click)
enter_button.pack()

# Frame 2: Display Selected Facility Information
frame2 = tk.Frame(root)
frame2.pack(pady=20)

facility_name_var = tk.StringVar()
institution_name_var = tk.StringVar()
institution_id_var = tk.StringVar()
label2_text = tk.StringVar()

label2 = tk.Label(frame2, textvariable=label2_text, wraplength=700)

# Create the Plotly graph and get the image buffer
image_buf = create_plotly_graph()

# Load the image from the buffer
img = Image.open(image_buf)
img = ImageTk.PhotoImage(img)

# Create a label to display the image
image_label = tk.Label(root, image=img)
image_label.pack(pady=20)


def display_graph(url):
   webbrowser.open_new_tab(url)

#Create a Label to display the link
link = Label(root, text="http://127.0.0.1:5400/",font=('Helveticabold', 15), fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e:
display_graph("http://127.0.0.1:5400/"))

# Start the main tkinter event loop
root.mainloop()
