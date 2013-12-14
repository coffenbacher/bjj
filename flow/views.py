from django.shortcuts import render
from flow.models import Flow

def show(request, id):
    f = Flow.objects.get(id=id)
    return render(request, 'flow/show.html', {'f': f})
