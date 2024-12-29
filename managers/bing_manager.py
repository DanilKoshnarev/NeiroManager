import requests
import json

class BingManager:
    def __init__(self):
        with open("config/secrets.json") as f:
            secrets = json.load(f)
        self.api_key = secrets["bing_api_key"]

    def generate_response(self, prompt):
        url = "https://api.bing.microsoft.com/v7.0/ai"
        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        data = {"query": prompt}
        response = requests.post(url, headers=headers, json=data)
        return response.json()