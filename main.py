from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import google.generativeai as genai
import io
import base64

# Configure the API key for Google Generative AI
api_key = "AIzaSyCLHwVq8sA02yRIa_pJrgU6OoZ-QecSjGo"
genai.configure(api_key=api_key)

# Initialize FastAPI app
app = FastAPI()


# Endpoint to process the image and prompt
@app.post("/generate_description/")
async def generate_description(prompt: str, file: UploadFile = File(...)):
    try:
        # Open the uploaded image file
        img = Image.open(io.BytesIO(await file.read()))
        
        # Convert image to base64
        # img_base64 = image_to_base64(img)
        
        # Use the Generative Model with prompt and image
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Assuming 'generate_content' can accept the base64 image and prompt, adjust if needed
        response = model.generate_content([prompt, img])
        
        # Return the generated response text
        return JSONResponse(content={"description": response.text})
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
