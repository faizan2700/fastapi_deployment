import os 
import requests 
from dotenv import load_dotenv 
load_dotenv('../.env')

class HFAgent: 
    def __init__(self): 
        self.api_key = os.getenv('HUGGING_FACE_API_KEY') 
        self.api_url = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest" 
        self.headers = {"Authorization": f"Bearer {self.api_key}"} 

    def get_response(self, user_input): 
        data = {"inputs": user_input}
        response = requests.post(self.api_url, headers=self.headers, json=data) 
        return response.json()[0][0].get('label', None)  

if __name__=='__main__': 
    agent = HFAgent() 
    while True: 
        user_input = input("You: ") 
        response = agent.get_response(user_input) 
        print(f"AI: {response}") 