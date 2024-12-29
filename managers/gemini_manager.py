import requests
import json

class GeminiManager:
    def __init__(self):
        with open("config/secrets.json") as f:
            secrets = json.load(f)
        self.api_key = secrets["gemini_api_key"]

    def generate_response(self, prompt):
        url = "https://gemini.api.url"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"input": prompt}
        response = requests.post(url, headers=headers, json=data)
        return response.json()