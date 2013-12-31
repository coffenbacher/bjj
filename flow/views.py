from django.core import serializers
from django.shortcuts import render, redirect
from flow.models import *
from django.http import HttpResponse
from json import dumps

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

def json(request, id):
    f = Flow.objects.get(id=id)
    nodes = [t.render_to_json() for  t in f.techniques.all()]
    links = []
    for t in f.techniques.all():
        links.extend(t.render_links_to_json())
    js = dumps({"nodes": nodes, "links": links})
    return HttpResponse(js, content_type="application/json")
