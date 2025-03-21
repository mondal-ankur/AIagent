from dotenv import load_dotenv  # Import the load_dotenv function from the dotenv library

load_dotenv()  # Load environment variables from a .env file
import os  # Import the os module for interacting with the operating system

# Retrieve API keys from environment variables
gemini_api = os.getenv("GEMINI_API_KEY")  # Get the Gemini API key from the environment (https://aistudio.google.com/apikey)
serper_api = os.getenv("SERPER_API_KEY")  # Get the Serper API key from the environment (https://serper.dev/billing)
