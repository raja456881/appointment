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

app.autodiscover_tasks()
