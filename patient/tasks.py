from celery import shared_task
from twilio.rest import Client
import time
import json
from decouple import config

@shared_task(bind=True)
def send_reminder_patient(self, phone):
    Accound_sid=config("Accound_sid")
    Auth_token=config("Auth_token")
    phone_no =config("phone_no")
    client = Client(Accound_sid, Auth_token)
    client.messages.create(from_=phone_no,
                      to=phone,
                      body='This is ur remainder for ur appointment  plz be available on your before schedule time')    
    return phone
