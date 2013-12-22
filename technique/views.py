from django.shortcuts import render, redirect
from models import *

# Create your views here.

def index(request):
    ts = Technique.objects.all()
    if 'name' in request.GET:
        ts = ts.filter(name__icontains=request.GET['name'])
    if 'category' in request.GET:
        ts = ts.filter(category__icontains=request.GET['category'])
    return render(request, 'technique/index.html', {'techniques': ts})

def show(request, id):
    t = Technique.objects.get(id=id)
    return render(request, 'technique/show.html', {'t': t})

def create(request):
    if request.method == 'POST':
        form = TechniqueForm(request.POST)
        if form.is_valid():
            t = form.save()
            return redirect('/technique/%s/' % t.id)
    else:
        form = TechniqueForm()
    return render(request, 'technique/create.html', {'form': form})
