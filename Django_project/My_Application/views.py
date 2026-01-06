from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    msg="<h1>Welcome to Django Framework</h1>"
    return HttpResponse(msg)

def index(request):
    return HttpResponse("<h1this is Index page/h1>")
