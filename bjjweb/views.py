from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

def index(request):
    return render(request, 'index.html', {})

def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('/?invalid_login=true')

