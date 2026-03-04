import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel("gemini-2.5-flash")


def ask_llm(prompt: str):
    """
    Sends a prompt to Gemini and returns the text response.
    """

    try:
        response = model.generate_content(prompt)

        if response and response.text:
            return response.text
        else:
            return "No response from LLM."

    except Exception as e:
        return f"LLM Error: {str(e)}"