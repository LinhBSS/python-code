import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def configure_model():
    genai.configure(api_key=GEMINI_API_KEY)
    return genai.GenerativeModel('gemini-2.0-flash')

generative_text_model = configure_model()

def generate_text(query: str):
    response = generative_text_model.generate_content(query)
    return {"text": response.text}

print(generate_text("Hello gemini"))