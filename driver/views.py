from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from driver.models import Inspection, Refilling, Driver, Vehicle
from accounts.decorators import driver_required
from django.http import HttpResponse
from driver.forms import InspectionForm, RefillingForm
from staff.models import Request
from workshop.models import Maintainance
from workshop.forms import MaintenanceForm

# Create your views here.

def driver(request):
    return render(request, 'driver_index.html', {})


def trip(request):
    tripss = Request.objects.all()
    mapbox_access_token = 'pk.eyJ1IjoiaWRhdmVyczk4IiwiYSI6ImNrcXBzZWxmczA4Mm8ydnEzMXR3emt3eXcifQ.d-QVNcLt_5acuWmgUpBPTA'
    return render(request, 'trip.html', {'trip': tripss, 'mapbox_access_token': mapbox_access_token})


def inspection(request):
    if request.method == 'POST':
        form = InspectionForm(request.POST)

        Inspection.objects.create(date=request.POST['date'], license=request.POST['number'],
                                  driver=request.POST['driver'], odometer=request.POST['odometer'],
                                  defect=request.POST['defect'])
        # steering=request.POST['steering'], brakes=request.POST['brakes'],
        # indicators=request.POST['indicators'], speedometer=request.POST['speedometer'],
        # wipers=request.POST['wipers'], body_interior=request.POST['interior'],
        # extinguisher=request.POST['extinguisher'],
        # first_aid=request.POST['firstaid'], floor_traps=request.POST['floor'],
        # emergency=request.POST['emergency'], passenger_door=request.POST['passenger'],
        # mirrors=request.POST['mirrors'],
        # body_exterior=request.POST['exterior'], discs=request.POST['discs'],
        # inflation=request.POST['inflation'], spare_wheel=request.POST['spare'],
        # fixing=request.POST['fixing'],
        # engine=request.POST['engine'], battery=request.POST['battery'],
        # exhaust=request.POST['exhaust'], reflectors=request.POST['reflectors'],

        if form.is_valid():
            form.save()
        return redirect('drivers:inspection')

    inspect = Inspection.objects.all()
    tripss = Vehicle.objects.all()
    drvr = Driver.objects.all()

    return render(request, 'inspection.html', {'insp': inspect, 'vehicle': tripss, 'driver': drvr})


def refilling(request):
    if request.method == 'POST':
        form = RefillingForm(request.POST)
        Refilling.objects.create(towards=request.POST['kwenda'], fuel=request.POST['aina'],
                                 liters=request.POST['kiasi'], vehicle=request.POST['gari'])
        if form.is_valid():
            form.save()
        return redirect('drivers:refilling')

    refill = Refilling.objects.all()
    drv = Driver.objects.all()
    vhc = Vehicle.objects.all()

    return render(request, 'refilling.html', {'refill': refill, 'driver': drv, 'vehicle': vhc})


def maintenance(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        Maintainance.objects.create(date=request.POST['date'], vehicle=request.POST['number'],
                                    driver=request.POST['driver'],
                                    mtype=request.POST['type'], description=request.POST['description'])
        if form.is_valid():
            form.save()
        return redirect('drivers:maintenance')
    else:
        tripss = Vehicle.objects.all()
        drvr = Driver.objects.all()
        return render(request, 'drmaintenance.html', {'vehicle': tripss, 'driver': drvr})
