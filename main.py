import os
from google import genai

API_KEY = os.environ.get('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY environment variable is not set")

client = genai.Client(api_key=API_KEY) 

response = client.models.generate_content(
    model="gemini-2.0-flash-exp",
    contents="How does AI work?",
)
print(response.text)