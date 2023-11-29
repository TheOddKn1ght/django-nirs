from django.contrib import admin
from .models import MedWorker, Procedure, Appointment, ProcedureJournal, AvailableDoctors, Patient

# Register your models here.

@admin.register(MedWorker)
class MedWorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'department', 'position')

@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_time', 'email', 'patient_id', 'doctor_id', 'room')

@admin.register(ProcedureJournal)
class ProcedureJournalAdmin(admin.ModelAdmin):
    list_display = ('id', 'procedure_id', 'patient_id', 'doctor_id', 'date', 'room', 'anamnesis')

@admin.register(AvailableDoctors)
class AvailableDoctorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'department', 'available_time')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'email', 'doctor_id', 'anamnesis')