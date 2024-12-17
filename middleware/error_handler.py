from fastapi import Request 
class AutoErrorHandler: 
    def __init__(self):
        pass 

    async def __call__(self, request, call_next): 
        try: 
            response = await call_next(request) 
        except Exception as error: 
            return {'error': str(error), 'status': '400'} 
         