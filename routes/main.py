import os 
from fastapi import FastAPI, Request, Response, HTTPException, APIRouter, Query 
import requests
from dotenv import load_dotenv  
load_dotenv('./.env') 

from whatsapp_service import WhatsappService
from Agent import Assistant 
from fastapi.responses import HTMLResponse 


router = APIRouter() 
whatsapp_service = WhatsappService()  
assitant = Assistant() 
assitant.get_response('how are you') 
@router.get('/webhook') 
async def verification_for_webhook(
    mode: str = Query(None, alias="hub.mode"), 
    token: str = Query(None, alias='hub.verify_token'), 
    challenge: str = Query(None, alias='hub.challenge')
):  
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
    num, msg = whatsapp_service.get_message(payload)
    print(f'webhook received num:{num}, msg:{msg}') 
    if num is None or msg is None: 
        return {'status': 200} 
    whatsapp_service.send_message(num, msg) 
    return {'status': 200} 

@router.post('/send_message') 
async def send_whatsapp_message(request: Request): 
    data = await request.json() 
    try:  
        num, msg = data.get('number'), data.get('message') 
    except Exception: 
        raise HTTPException(status_code=400, detail='number and message are necessary!') 
    resp = assitant.get_response(msg) 
    response = whatsapp_service.send_message(num, message_body=resp) 
    return {'status': 200, 'message': response} 

@router.post('/get_response') 
async def get_ai_response(request: Request): 
    data = await request.json()
    try:
        msg = data.get('message')
    except Exception:
        raise HTTPException(status_code=400, detail='message is necessary!')
    resp = assitant.get_response(msg)
    return {'status': 200, 'message': resp}

 
