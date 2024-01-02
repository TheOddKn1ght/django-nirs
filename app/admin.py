from django.contrib import admin
from .models import Doctor, Appointment, Procedure, Patient, ProcedureLog, MedicalStaff

# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'department', 'time')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_time', 'email', 'patient_id', 'doctor_id', 'room')

@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'phone', 'email', 'doctor_id', 'medical_history')

@admin.register(ProcedureLog)
class ProcedureLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_id', 'doctor_id', 'date', 'room', 'medical_history')

@admin.register(MedicalStaff)
class MedicalStaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'phone', 'department', 'position')