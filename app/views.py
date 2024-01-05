from django.shortcuts import render, get_object_or_404, redirect
from .models import MedicalStaff, Procedure, Doctor
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.

def index(request):
    return render(request, 'index.html')

def services(request):
    procedures = Procedure.objects.all()
    return render(request, 'services.html', {'procedures': procedures})

def service_detail(request, service_id):
    service = get_object_or_404(Procedure, pk=service_id)
    return render(request, 'service_detail.html', {'service': service})

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def doctors(request):
    doctors_list = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors_list})

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, 'doctor_detail.html', {'doctor': doctor})

def about(request):
    return render(request, "about.html")

def contacts(request):
    return render(request, "contact.html")

def book_appointment(request):
    if request.method == 'POST':
        # Process the form submission here
        # You can access the client's credentials using request.POST['name'], request.POST['email'], etc.
        # Implement your logic for booking the appointment

        # Redirect or render a success page
        return render(request, 'index.html')

    # If the request method is not POST, you may want to handle it differently
    # For example, redirect to the service detail page or show an error message
    return render(request, 'index.html')

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to the desired page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to the desired page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})