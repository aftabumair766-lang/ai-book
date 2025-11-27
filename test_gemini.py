import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro:generateContent?key={API_KEY}"

response = requests.get(url)
print("Status code:", response.status_code)
print("Response text:", response.text)
