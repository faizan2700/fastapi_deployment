import os 
from fastapi import FastAPI, Request, Response, HTTPException 
import requests
from dotenv import load_dotenv 
from whatsapp_service import WhatsappService
from Agent import Assistant 
from fastapi.responses import HTMLResponse 

class Route: 
    pass 