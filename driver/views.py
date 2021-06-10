from django.shortcuts import render
from driver.models import Assigned
from django.http import HttpResponse


# Create your views here.
def driver(request):
    return render(request, 'driver_index.html', {})


def trip(request):
    tripss = Assigned.objects.all()
    return render(request, 'trip.html', {'trip': tripss})
