from rest_framework import serializers
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from datetime import datetime, timedelta
import time

from .models import *
import json


class AppointmentSerializer(serializers.ModelSerializer):


    class Meta:
        model =Appointment
        fields="__all__"


    def to_representation(self, instance):
        data = dict(super(AppointmentSerializer, self).to_representation(instance))
        print(data, "=-----------")
        data["doctor"]=instance.doctor.username
        data["patient"]=instance.patient.username
        return data



    def create(self, validate_data):
        data = super(AppointmentSerializer, self).create(validate_data)
        last_four = str(round(time.time() * 1000000000))[-4:]
        datetime_str=str(data.appointment_time)
        fatat=data.appointment_time.strftime("%Y-%m-%d %H:%M:%S")
        date_part, time_part= fatat.split()
        hour, minute1, _ = time_part.split(':')
        dt = datetime.fromisoformat(datetime_str[:-6])

        one_day = timedelta(days=1)
        result_str = dt.strftime("%Y-%m-%d %H:%M:%S")
        date_part, time_part= result_str.split()
        hour, _, _ = time_part.split(':')
       
        result_date = dt - one_day
        result_str = result_date.strftime("%Y-%m-%d %H:%M:%S")
        date_part, time_part = result_str.split()
        year, month, day = date_part.split('-')
        hour, _, _ = time_part.split(':')

        schedule, created = CrontabSchedule.objects.get_or_create(hour=int(hour),minute =minute1,day_of_month=int(day),month_of_year=int(month))
        PeriodicTask.objects.create(crontab=schedule, name=f"{last_four}-1-days-before", task="patient.tasks.send_reminder_patient", args=json.dumps([f'+91{data.patient.phone}']))

        two_day = timedelta(days=2)
        last_four = str(round(time.time() * 1000000000))[-4:]
        result_date = dt - two_day
        result_str = result_date.strftime("%Y-%m-%d %H:%M:%S")
        date_part, time_part = result_str.split()
        year, month, day = date_part.split('-')
        hour, _, _ = time_part.split(':')#, args = json.dumps([[2,3]]))
        schedule, created = CrontabSchedule.objects.get_or_create(hour=int(hour), minute =minute1,day_of_month=int(day),month_of_year=int(month))
        PeriodicTask.objects.create(crontab=schedule, name=f"{last_four}-2-days-before", task="patient.tasks.send_reminder_patient", args=json.dumps([f'+91{data.patient.phone}']))
        
        two_hours= timedelta(hours=2)
        result_date = dt - two_hours
        result_str = result_date.strftime("%Y-%m-%d %H:%M:%S")
        date_part, time_part = result_str.split()
        last_four = str(round(time.time() * 1000000000))[-4:]
        year, month, day = date_part.split('-')
        hour, _, _ = time_part.split(':')#, args = json.dumps([[2,3]]))
        schedule, created = CrontabSchedule.objects.get_or_create(hour=int(hour), minute =int(minute1),day_of_month=int(day),month_of_year=int(month))
        PeriodicTask.objects.create(crontab=schedule, name=f"{last_four}-2-hours-before", task="patient.tasks.send_reminder_patient", args=json.dumps([f'+91{data.patient.phone}']))
        return data
       

    

