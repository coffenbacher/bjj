from django.shortcuts import render
from models import *

# Create your views here.

def show(request, id):
    t = Technique.objects.get(id=id)
    return render(request, 'technique/show.html', {'t': t})
