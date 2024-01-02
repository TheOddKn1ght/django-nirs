from django.contrib.auth.models import User
from django.db import models

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    time = models.DateTimeField()

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField()
    email = models.EmailField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    room = models.IntegerField()

class Procedure(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    doctor_id = models.IntegerField()
    medical_history = models.TextField()

class ProcedureLog(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    date = models.DateTimeField()
    room = models.IntegerField()
    medical_history = models.TextField()

class MedicalStaff(models.Model):
    id = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=255)
    position = models.CharField(max_length=255)