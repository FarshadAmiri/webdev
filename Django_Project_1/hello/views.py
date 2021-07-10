from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    return HttpResponse(f'Hello, World!')

# def greet(request, name):
#     return HttpResponse(f'Hello, {name.capitalize()}!')

def greet(request, name):
    return render(request, "hello/greet.html", {"name" : name.capitalize()})

def sample(request):
    return render(request, "sample/index.html")