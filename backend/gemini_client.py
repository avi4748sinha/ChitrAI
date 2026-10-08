import os
from dotenv import load_dotenv
from google import genai

load_dotenv()  # .env file padhke values load karta hai

# client: Gemini se baat karne wala object. Key .env se aati hai, code mein likhi nahi
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Model ka naam bhi .env se. Nahi mila to default use hoga
IMAGE_MODEL = os.getenv("GEMINI_IMAGE_MODEL", "gemini-2.5-flash-image")

# filhal no use iska 