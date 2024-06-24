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
