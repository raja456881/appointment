from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from twilio.rest import Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appointment.settings')

app = Celery('appointment')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
# app.conf.beat_schedule = {
#     'send-mail-every-day-at-8': {
#         'task': 'send_mail_app.tasks.send_mail_func',
#         'schedule': crontab(hour=0, minute=46, day_of_month=19, month_of_year = 6),
#         #'args': (2,)
#     }
    
# }

# Celery Schedules - https://docs.celeryproject.org/en/stable/reference/celery.schedules.html

app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')

# @app.task(bind=True)
# def debug_task(self):
#     print("jkkkkkkkkkkkkkkkkkkkkkkkkkkk")
#     Accound_sid="AC964153c50c3304ed945eb665c9905d2b"
#     Auth_token="57e2db03c98b0e4f79e00bb2f3fb7b4e"
#     phone_no =+19377779771
#     client = Client(Accound_sid, Auth_token)
#     client.messages.create(from_=phone_no,
#                       to=+917982809688,
#                       body='xzcxsdvcvdsvfdgf')  
