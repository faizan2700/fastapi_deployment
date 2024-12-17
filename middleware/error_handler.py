from fastapi.exceptions import HTTPException 

class AutoErrorHandler: 
    def __init__(self, app): 
        self.app = app 

    async def __call__(self, scope, receive, send): 
        try: 
            await self.app(scope, receive, send) 
        except Exception as error: 
            raise HTTPException(status_code=400) 