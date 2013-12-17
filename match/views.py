from django.shortcuts import render
from models import *

def index(request):
    ms = Match.objects.all()
    return render(request, 'match/index.html',{'matches': ms})
