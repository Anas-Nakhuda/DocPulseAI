import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file FIRST
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ GOOGLE_API_KEY not found in .env file!")
else:
    genai.configure(api_key=api_key)
    print("✅ Available Models for your API Key:\n")
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            # Prints model identifiers (e.g., gemini-1.5-flash, gemini-2.0-flash, etc.)
            print(f"- {m.name.replace('models/', '')}")