from django.shortcuts import render, redirect
from flow.models import *

def index(request):
    f = Flow.objects.all()
    return render(request, 'flow/index.html', {'flows': f})


def show(request, id):
    f = Flow.objects.get(id=id)
    return render(request, 'flow/show.html', {'f': f})

def create(request):
    if request.method == 'POST':
        form = FlowForm(request.POST)
        if form.is_valid():
            f = form.save()
            return redirect('/flow/%s/' % f.id)
    else:
        form = FlowForm()
    return render(request, 'flow/create.html', {'form': form})
