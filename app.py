from fastapi import FastAPI 
from fastapi.responses import HTMLResponse 
from middleware import AutoErrorHandler 
from routes import router 


app1 = FastAPI()  
app1.include_router(router, prefix="/api")

@app1.get("/") 
def home(): 
    return HTMLResponse('<h1>Hello World</h1>')  

app = AutoErrorHandler(app1) 