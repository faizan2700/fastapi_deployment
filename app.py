from fastapi import FastAPI 
from fastapi.responses import HTMLResponse 
from middleware import AutoErrorHandler  
from starlette.middleware.base import BaseHTTPMiddleware 
from routes import router 


app = FastAPI()  
app.include_router(router, prefix="/api")

@app.get("/") 
def home(): 
    return HTMLResponse('<h1>Hello World</h1>')  

error_handling = AutoErrorHandler()
app.add_middleware(BaseHTTPMiddleware, dispatch=error_handling) 
