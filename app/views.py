from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def service_detail(request, service_id):
    return render(request, 'service_detail.html', {'service_id': service_id})

def custom_404(request, exception):
    return render(request, '404.html', status=404)