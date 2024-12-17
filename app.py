from fastapi import FastAPI 
from fastapi.responses import HTMLResponse 

app = FastAPI() 

@app.get("/") 
def home(): 
    return HTMLResponse('<h1>Hello World</h1>') 