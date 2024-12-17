from fastapi import FastAPI 
from fastapi.responses import HTMLResponse 
from routes.main import * 

app = FastAPI() 

@app.get("/") 
def home(): 
    return HTMLResponse('<h1>Hello World</h1>') 