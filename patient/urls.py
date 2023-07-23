
from django.urls import path
from .views import *

urlpatterns = [
    path("",CreateAppointmentApiview.as_view(), name="AppointmentApiview"),
]
