from django.shortcuts import render
from models import *

def index(request):
    ms = Match.objects.all()
    return render(request, 'match/index.html',{'matches': ms})

def show(request, id):
    m = Match.objects.get(id=id)
    return render(request, 'match/show.html', {'m': m})
