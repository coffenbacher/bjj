from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from technique.models import *

def index(request):
    techniques = Technique.objects.all()
    return render(request, 'index.html', {'techniques': techniques})

def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('/?invalid_login=true')
