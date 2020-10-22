from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel
# Create your views here.


def sightings(request):
    squirrels=Squirrel.objects.all()[:100]
    context={
            'squirrels':squirrels
            }
    return render(request,'sightings.html',context)
        
"""
def index(request):
    return render(request,'sightings/index.html',{})
"""
