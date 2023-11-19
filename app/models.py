from django.contrib.auth.models import User
from django.db import models

class MedicalStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    education = models.CharField(max_length=255)

class Doctor(models.Model):
    medical_staff = models.OneToOneField(MedicalStaff, on_delete=models.CASCADE)

class Reception(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Procedure(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    room_number = models.IntegerField()
    invoice_number = models.IntegerField(null=True, blank=True)
    medical_staff = models.ForeignKey(MedicalStaff, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

class Price(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    procedure = models.OneToOneField(Procedure, on_delete=models.CASCADE)

class TotalCost(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PatientRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

class DoctorCatalog(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)

class ProcedureCatalog(models.Model):
    procedure = models.OneToOneField(Procedure, on_delete=models.CASCADE)

class MedicalStaffCatalog(models.Model):
    medical_staff = models.OneToOneField(MedicalStaff, on_delete=models.CASCADE)