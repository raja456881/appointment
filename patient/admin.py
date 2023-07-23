from django.contrib import admin
from.models import *

# Register your models here.
# class Appointmentadmin(admin.ModelAdmin):
#     list_display=("doctor__usrname","patient__username" "appointment_time")
#     search_fields = ("doctor_name__username","patient__username" "appointment_time")

admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(Doctor)