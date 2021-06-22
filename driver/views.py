from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from driver.models import Inspection
from driver.models import Assigned
from accounts.decorators import driver_required
from django.http import HttpResponse
from driver.forms import InspectionForm


# Create your views here.

def driver(request):
    return render(request, 'driver_index.html', {})


def trip(request):
    tripss = Assigned.objects.all()
    return render(request, 'trip.html', {'trip': tripss})


def inspection(request):
    if request.method == 'POST':
        form = InspectionForm(request.POST)
        Inspection.objects.create(horn=request.POST['horn'], lice_plate_condition=request.POST['licence'],
                                  steering=request.POST['steering'], brakes=request.POST['brakes'],
                                  indicators=request.POST['indicators'], speedometer=request.POST['speedometer'],
                                  wipers=request.POST['wipers'], body_interior=request.POST['interior'],
                                  extinguisher=request.POST['extinguisher'],
                                  first_aid=request.POST['firstaid'], floor_traps=request.POST['floor'],
                                  emergency=request.POST['emergency'], passenger_door=request.POST['passenger'],
                                  mirrors=request.POST['mirrors'],
                                  body_exterior=request.POST['exterior'], discs=request.POST['discs'],
                                  inflation=request.POST['inflation'], spare_wheel=request.POST['spare'],
                                  fixing=request.POST['fixing'],
                                  engine=request.POST['engine'], battery=request.POST['battery'],
                                  exhaust=request.POST['exhaust'], reflectors=request.POST['reflectors'],
                                  defect=request.POST['defect'], action=request.POST['measures'])
        if form.is_valid():
            form.save()
        return redirect('drivers:inspection')

    inspect = Inspection.objects.all()
    return render(request, 'inspection.html', {'insp': inspect})


def refilling(request):
    return render(request, 'refilling.html', {})
