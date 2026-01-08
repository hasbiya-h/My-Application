from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def home(request):
    context = {
        'name': 'Hasbiya'
    }
    return render(request, 'my_application/home.html', context)

def index(request):
    return render(request, 'my_application/index.html')

def user(request):
    return render(request, 'my_application/users.html')