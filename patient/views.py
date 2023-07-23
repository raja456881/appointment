from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import *
from .searilizers import AppointmentSerializer
from django_celery_beat.models import PeriodicTask, CrontabSchedule

# Create your views here.


class CreateAppointmentApiview(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


