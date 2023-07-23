from django.db import models
# Create your models here.



class Patient(models.Model):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=100, blank=True, null=True)
    phone=models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.username)

class Doctor(models.Model):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=100, blank=True, null=True)
    phone=models.CharField(max_length=10, blank=True, null=True)
    

    def __str__(self):
       return  str(self.username)






class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE, related_name="doctor_user")
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE, related_name="patient_user")
    appointment_time=models.DateTimeField()

    def __str__(self):
        return str(self.appointment_time)








    