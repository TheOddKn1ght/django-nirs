from django.contrib.auth.models import User
from django.db import models

class MedWorker(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

class Procedure(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField()
    email = models.EmailField()
    patient_id = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor_id = models.ForeignKey('MedWorker', on_delete=models.CASCADE)
    room = models.CharField(max_length=255)

class ProcedureJournal(models.Model):
    id = models.AutoField(primary_key=True)
    procedure_id = models.ForeignKey('Procedure', on_delete=models.CASCADE)
    patient_id = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor_id = models.ForeignKey('MedWorker', on_delete=models.CASCADE)
    date = models.DateField()
    room = models.CharField(max_length=255)
    anamnesis = models.TextField()

class AvailableDoctors(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    available_time = models.CharField(max_length=255)

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    doctor_id = models.ForeignKey('MedWorker', on_delete=models.CASCADE)
    anamnesis = models.TextField()
