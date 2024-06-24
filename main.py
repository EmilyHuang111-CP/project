import tkinter as tk
from tkinter import ttk, messagebox
from locator import active_facility_id_name, match_facility_name, match_institution_name, match_institution_id
from plotly_graph import *
import webbrowser
from PIL import Image, ImageTk

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
new_size = (800, 800)
resized_image = img.resize(new_size, Image.LANCZOS)
tk_image = ImageTk.PhotoImage(resized_image)

# Create a Canvas widget
canvas = tk.Canvas(root, width=600, height=600)  # Adjust canvas size as needed
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create Scrollbars
h_scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
v_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure canvas scrolling
canvas.configure(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)

# Create an image on the canvas
canvas_image = canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

# Configure the scroll region
canvas.config(scrollregion=canvas.bbox(tk.ALL))

def display_graph(url):
   webbrowser.open_new_tab(url)

#Create a Label to display the link
#make sure to run the plotly graph api code at the same time when running this "main.py" code
link = Label(root, text="Link to the graph",font=('Helveticabold', 15), fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e:
display_graph("http://127.0.0.1:5400/"))
canvas.create_window(10, 10, anchor=tk.NW, window=link)

# Start the main tkinter event loop
root.mainloop()

