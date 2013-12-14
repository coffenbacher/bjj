from django.shortcuts import render, redirect
from models import *

# Create your views here.

def all(request):
    ts = Technique.objects.all()
    return render(request, 'technique/all.html', {'ts': ts})

def show(request, id):
    t = Technique.objects.get(id=id)
    return render(request, 'technique/show.html', {'t': t})

def create(request):
    if request.method == 'POST':
        form = TechniqueForm(request.POST)
        #Todo: this should be investigated, odd behavior for neo4django forms
        if form.is_valid():
            t = form.save()
            return redirect('/technique/%s/' % t.id)
    else:
        form = TechniqueForm()
    return render(request, 'technique/create.html', {'form': form})
