from django.contrib import admin
from .models import Doctor, MedicalStaff, Procedure, Patient, ProcedureLog, Appointment

# Updated DoctorAdmin
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_full_name', 'department', 'time')

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.second_name + ' ' if obj.second_name else ''}{obj.last_name}"
    get_full_name.short_description = 'Full Name'

# Updated MedicalStaffAdmin
@admin.register(MedicalStaff)
class MedicalStaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_full_name', 'phone', 'department', 'position')

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.second_name + ' ' if obj.second_name else ''}{obj.last_name}"
    get_full_name.short_description = 'Full Name'

# Unchanged ProcedureAdmin
@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost')

# Unchanged PatientAdmin
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_full_name', 'phone', 'email', 'doctor_id', 'medical_history')

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.second_name + ' ' if obj.second_name else ''}{obj.last_name}"
    get_full_name.short_description = 'Full Name'

# Unchanged ProcedureLogAdmin
@admin.register(ProcedureLog)
class ProcedureLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_id', 'doctor_id', 'date', 'room', 'medical_history')

# Unchanged AppointmentAdmin
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_time', 'email', 'patient_id', 'doctor_id', 'room')
