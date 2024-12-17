import os 
from fastapi import FastAPI, Request, Response, HTTPException, APIRouter 
import requests
from dotenv import load_dotenv 
from whatsapp_service import WhatsappService
from Agent import Assistant 
from fastapi.responses import HTMLResponse 

router = APIRouter() 

@router.get('/webhook') 
async def verification_for_webhook(request: Request): 
    return {'status': 200, 'message': 'Verified!'} 

@router.post('/webhook') 
async def handle_webhook_payload(request: Request): 
    payload = await request.json() 
    return {'status': 200, 'message': payload} 

@router.post('/send_message') 
async def send_whatsapp_message(request: Request): 
    payload = await request.json()  
    return {'status': 200, 'message': payload} 

 
