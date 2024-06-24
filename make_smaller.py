from PIL import Image, ImageTk

# Load the image from the buffer
img = Image.open(image_buf)
new_size = (200,200)
resized_image = img.resize(new_size, Image.LANCZOS)
tk_image = ImageTk.PhotoImage(resized_image)

# Create a label to display the image
image_label = tk.Label(root, image=tk_image)
image_label.pack(pady=20)
