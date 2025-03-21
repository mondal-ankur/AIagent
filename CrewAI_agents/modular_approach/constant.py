from dotenv import load_dotenv

load_dotenv()
import os

gemini_api = os.getenv("GEMINI_API_KEY") # https://aistudio.google.com/apikey
serper_api = os.getenv("SERPER_API_KEY") # https://serper.dev/billing
