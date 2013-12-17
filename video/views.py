# Create your views here.
from django.shortcuts import render
from video.models import Video

#def index(request):
#    return render(request, 'all.html', {'vs': vs})

def show(request, id):
    v = Video.objects.get(id=id)
    return render(request, 'video/show.html', {'v': v})
