import requests
import json 
import os 
from utils.get_keys import load_config

class GeminiModel:
    def __init__(self, system_prompt='', temperature=0):
        load_config("configs/config.yaml")

        self.system_prompt = system_prompt
        self.temperature = temperature
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model_endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"
        self.headers = {"Content-Type": "application/json"}
        

    def generate_response(self, user_input):
        payload = {
            "contents": [{
                "parts": [{
                    "text": user_input
                }]
            }]
        }

        try:
            request = requests.post(
                self.model_endpoint,
                headers=self.headers,
                data=json.dumps(payload)
            )
            
            if request.status_code != 200:
                return {"error": f"API request failed with status {request.status_code}: {request.text}"}
                
            request_json = request.json()
            response = request_json["candidates"][0]["content"]["parts"][0]["text"]
            return {"response": response}

        except requests.RequestException as e:
            return {"error": f"Error in invoking model! {str(e)}"}