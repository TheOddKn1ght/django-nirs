from django.contrib import admin
from .models import MedicalStaff, Doctor, Reception, Procedure, Price, TotalCost, PatientRecord, DoctorCatalog, ProcedureCatalog, MedicalStaffCatalog
# Register your models here.

admin.site.register(MedicalStaff)
admin.site.register(Doctor)
admin.site.register(Reception)
admin.site.register(Procedure)
admin.site.register(Price)
admin.site.register(TotalCost)
admin.site.register(PatientRecord)
admin.site.register(DoctorCatalog)
admin.site.register(ProcedureCatalog)
admin.site.register(MedicalStaffCatalog)