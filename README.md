# Image Captioning with Google Generative AI (Gemini 1.5 Flash)

This project uses **Google Generative AI (Gemini 1.5 Flash)** for generating captions based on uploaded images and prompts. The system integrates a **FastAPI** backend with a **Streamlit** frontend to deliver an interactive image captioning experience.

## Team Members
- **Ashreen Tabassum**  
- **M R Pranathi**  
- **S Shreeshta Reddy**  

---

## Features

- Upload images in `PNG`, `JPG`, or `JPEG` formats.  
- Use text prompts to customize caption generation.  
- Generate captions using Google Generative AI (Gemini 1.5 Flash).  
- FastAPI backend for handling image processing and model requests.  
- Interactive Streamlit interface for user interaction.  

---

## Installation Instructions

### Prerequisites
Ensure the following are installed on your system:
- Python 3.8 or higher
- `pip` for package management
- A valid **Google API Key** for Generative AI (Gemini 1.5)

### Steps to Set Up the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/image-captioning-ai.git
   cd image-captioning-ai
2. **Configure the Google API Key**  
   Install all required Python libraries:
   ```bash
   pip install -r requirements.txt
3. **Replace the placeholder api_key in main.py with your own API key:**  
   Install all required Python libraries:
   ```bash
   api_key = "YOUR_GOOGLE_API_KEY"
4. **Run the FastAPI Backend**  
   Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
5. **Run the Streamlit Frontend**  
   Open a new terminal and start the Streamlit application:
   ```bash
   streamlit run app.py

## Testing Instructions

### 1. Test the Backend via Swagger UI

1. Open your web browser and navigate to the FastAPI documentation:  
   [http://127.0.0.1:8000/docs]

2. In the Swagger UI interface:
   - Locate the `/generate_description/` endpoint.
   - Click the **"Try it out"** button.
   - Upload a valid image file under the **file** field.
   - Provide a text prompt in the **prompt** field (e.g., `"Generate a short description for the given image"`).
   - Click the **"Execute"** button.

3. Verify the response in the JSON output section:
   - Ensure the `description` field contains the generated caption for the uploaded image.

### 2. Test the Frontend via Streamlit

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
2. Navigate to http://localhost:8501 in your browser.
3. Upload an image and provide a prompt in the interface.
4. Click GET RESPONSE and verify the caption generated is relevant to the uploaded image.

### 3.Sampl Output
