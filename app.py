from fastapi import FastAPI 
from fastapi.responses import HTMLResponse 
from routes import router 

app = FastAPI()  
app.include_router(router, prefix="/api")

@app.get("/") 
def home(): 
    return HTMLResponse('<h1>Hello World</h1>') 