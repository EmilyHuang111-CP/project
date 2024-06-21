import plotly.express as px
import pandas as pd
from PIL import Image, ImageTk
import io
from tkinter import Tk, Label

# Function to create and save Plotly graph as an image
def create_plotly_graph():
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    # Save the Plotly figure to an image buffer
    img_buf = io.BytesIO()
    fig.write_image(img_buf, format='png')
    img_buf.seek(0)  # Rewind buffer to the beginning

    return img_buf
