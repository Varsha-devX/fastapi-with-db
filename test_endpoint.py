import requests
import json

url = "http://127.0.0.1:8000/ask"
headers = {"Content-Type": "application/json"}
data = {
    "message": "Tell me a joke.",
    "system_prompt": "You are a witty comedian."
}

try:
    response = requests.post(url, headers=headers, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
except Exception as e:
    print(f"An error occurred: {e}")
