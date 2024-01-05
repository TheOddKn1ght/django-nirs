from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, default='Unknown')
    second_name = models.CharField(max_length=50, blank=True, null=True, default='Unknown')
    last_name = models.CharField(max_length=50, default='Unknown')
    department = models.CharField(max_length=255)
    time = models.DateTimeField()
    photo = models.ImageField(upload_to='static/img/doctor_profile_pic', blank=True, null=True)

    def get_full_name(self):
        full_name = f"{self.first_name} {self.second_name + ' ' if self.second_name else ''}{self.last_name}"
        return full_name

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
    description = models.TextField()

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, default='Unknown')
    second_name = models.CharField(max_length=50, blank=True, null=True, default='Unknown')
    last_name = models.CharField(max_length=50, default='Unknown')
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    doctor_id = models.IntegerField()
    medical_history = models.TextField()

    @receiver(post_save, sender=User)
    def create_patient(sender, instance, created, **kwargs):
        if created and not instance.is_staff:
            Patient.objects.create(
                first_name=instance.first_name,
                second_name=instance.second_name,
                last_name=instance.last_name,
                phone='',  # Add appropriate default value
                email=instance.email,
                doctor_id=0,  # Add appropriate default value
                medical_history='',  # Add appropriate default value
            )

    post_save.connect(create_patient, sender=User)

class ProcedureLog(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    date = models.DateTimeField()
    room = models.IntegerField()
    medical_history = models.TextField()

class MedicalStaff(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, default='Unknown')
    second_name = models.CharField(max_length=50, blank=True, null=True, default='Unknown')
    last_name = models.CharField(max_length=50, default='Unknown')
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=255)
    position = models.CharField(max_length=255)