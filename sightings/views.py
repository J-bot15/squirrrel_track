from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import SquForm
from django.db.models import Count
# Create your views here.


def sightings(request):
    squirrels=Squirrel.objects.all()[:100]
    context={
            'squirrels':squirrels
            }
    return render(request,'sightings.html',context)


def map(request):
    sightings=Squirrel.objects.all()[:100]
    context={
            'sightings':sightings
            }
    return render(request,'map.html',context)

def add(request):
    if request.method=='POST':
        form=SquForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/sightings/')

    else:
        form=SquForm()
        context={'form':form}
    return render(request,'sightings/add.html',context)



def update(request,id):
    obj=get_object_or_404(Squirrel,unique_id=id)
    form=SquForm(request.POST,instance=obj)
    context={'form':form}
    if form.is_valid():
        form.save()
        return redirect('/sightings/')
    else:
        return render(request,'sightings/update.html',context)


def stats(request):
    total_sq = Squirrel.objects.count()
    am_amount = Squirrel.objects.all().filter(shift='AM').count()
    pm_amount = Squirrel.objects.all().filter(shift='PM').count()
    context = {
            'total_squirrel':total_sq,
            'am_amount':am_amount,
            'pm_amount':pm_amount,
            }
    return render(request, 'sightings/stats.html',context)

