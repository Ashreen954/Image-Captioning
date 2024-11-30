import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# FastAPI server URL
API_URL = "http://127.0.0.1:8000/generate_description/"


st.header("Image Caption Generation")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    st.image(Image.open(uploaded_file))

# Text input prompt
prompt = st.text_input("Enter a prompt")

# Button to trigger response
if st.button("GET RESPONSE"):
    if uploaded_file is not None and prompt:
        # Prepare the image and prompt for sending to FastAPI backend
        img_bytes = uploaded_file.getvalue()
        
        # Send the image and prompt to FastAPI
        response = requests.post(
            f"{API_URL}?prompt={prompt}",  # Pass the prompt as a query parameter
            files={"file": ("uploaded_image", img_bytes, "image/jpeg")}
        )

# Check the response status code and handle accordingly
        if response.status_code == 200:
            st.write("Generated Description:", response.json().get("description"))
        else:
            st.write("Error: ", response.text)

