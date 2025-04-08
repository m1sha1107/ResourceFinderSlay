import os
from flask import Blueprint
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("GEMINI_API_KEY not found in .env file.")
genai.configure(api_key=api_key)

# Initialize Flask Blueprint for routes
main = Blueprint("main", __name__)

# Example route (temporary for testing)
@main.route("/")
def home():
    return "Flask App is running and Gemini API is configured."
