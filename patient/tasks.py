from celery import shared_task
from twilio.rest import Client
import time
import json
# from decouple import config

@shared_task(bind=True)
def send_reminder_patient(self, phone):
    Accound_sid="AC28d8d98debaa39135dc71d67a03bd1fb"
    Auth_token="bdba2978ba41a8800885fbf5423b12a0"
    phone_no =+14327772801
    client = Client(Accound_sid, Auth_token)
    client.messages.create(from_=phone_no,
                      to=phone,
                      body='This is ur remainder for ur appointment  plz be available on your before schedule time')    
    return phone
