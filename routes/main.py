import os 
from fastapi import FastAPI, Request, Response, HTTPException, APIRouter, Query 
import requests
from dotenv import load_dotenv 
from whatsapp_service import WhatsappService
from Agent import Assistant 
from fastapi.responses import HTMLResponse 

router = APIRouter() 
whatsapp_service = WhatsappService() 
@router.get('/webhook') 
async def verification_for_webhook(mode: str = Query(None, alias="hub.mode"), token: str = Query(None, alias='hub.verify_token'), challenge: str = Query(None, alias='hub.challenge')):  
    print(f'Incoming request {token}, {mode}, {challenge}') 
    if mode == 'subscribe' and token == os.getenv('WHATSAPP_VERIFY_TOKEN'): 
        print(str(challenge)) 
        return int(challenge) 
    else: 
        error = f'mode={mode}, token={token}, challenge={challenge}'
        raise HTTPException(status_code=400, detail=str(error))  

@router.post('/webhook') 
async def handle_webhook_payload(request: Request): 
    payload = await request.json() 
    return {'status': 200, 'message': payload} 

@router.post('/send_message') 
async def send_whatsapp_message(request: Request): 
    payload = await request.json()  
    response = whatsapp_service.send_message('+919579591713', message_body='hello world!!!') 
    return {'status': 200, 'message': response} 

 
