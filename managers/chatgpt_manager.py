import openai
import json

class ChatGPTManager:
    def __init__(self):
        with open("config/secrets.json") as f:
            secrets = json.load(f)
        openai.api_key = secrets["chatgpt_api_key"]

    def generate_response(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]