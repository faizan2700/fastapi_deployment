class Assistant: 
    def __init__(self, model_name: str = "google-t5/t5-large"):
        ... 
    def get_response(self, user_input: str) -> str:
        # return self.model(user_input)[0].get('generated_text') 
        return user_input 