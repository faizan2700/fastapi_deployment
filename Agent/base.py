from transformers import pipeline 

class Assistant: 
    def __init__(self, model_name: str = "google-t5/t5-small"):
        self.model = pipeline("text2text-generation", model=model_name) 
    def get_response(self, user_input: str) -> str:
        return self.model(user_input)[0].get('generated_text') 
    
if __name__=='__main__': 
    assistant = Assistant()
    while True:
        user_input = input("You: ")
        response = assistant.get_response(user_input) 
        try: 
            print(f"AI: {response[0].get('generated_text')}") 
        except Exception as error: 
            print(f'AI unavailable: {error}') 