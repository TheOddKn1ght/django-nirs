from django.shortcuts import render, get_object_or_404
from .models import MedWorker

# Create your views here.

def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def service_detail(request, service_id):
    return render(request, 'service_detail.html', {'service_id': service_id})

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def doctors(request):
    doctors_list = MedWorker.objects.filter(position='Doctor')
    return render(request, 'doctors.html', {'doctors': doctors_list})

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(MedWorker, pk=doctor_id) # This is shit. TODO: make a separate table
    return render(request, 'doctor_detail.html', {'doctor': doctor})