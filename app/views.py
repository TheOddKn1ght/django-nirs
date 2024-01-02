from django.shortcuts import render, get_object_or_404
from .models import MedicalStaff, Procedure


# Create your views here.

def index(request):
    return render(request, 'index.html')

def services(request):
    procedures_list = Procedure.objects.all()
    return render(request, 'services.html', {'procedures': procedures_list})

def service_detail(request, service_id):
    service = get_object_or_404(Procedure, pk=service_id)
    return render(request, 'service_detail.html', {'service': service})

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def doctors(request):
    doctors_list = MedicalStaff.objects.filter(position='Doctor')
    return render(request, 'doctors.html', {'doctors': doctors_list})

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(MedicalStaff, pk=doctor_id)
    return render(request, 'doctor_detail.html', {'doctor': doctor})

def about(request):
    return render(request, "about.html")