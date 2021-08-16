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
from accounts.models import User


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

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
        return redirect('drivers:inspection')

    inspect = Inspection.objects.all()
    tripss = Vehicle.objects.all()
    drvr = Driver.objects.all()

    return render(request, 'inspection.html', {'insp': inspect, 'vehicle': tripss, 'driver': drvr})


def refilling(request):
    if request.method == 'POST':
        form = RefillingForm(request.POST)
        Refilling.objects.create(towards=request.POST['kwenda'], fuel=request.POST['aina'],
                                 liters=request.POST['kiasi'], vehicle=request.POST['gari'], driver=request.POST['driver'])
        if form.is_valid():
            instance = form.save(commit=False)
            instance.sent_by = request.user
        return redirect('drivers:refilling')
    users = User.objects.all()
    refill = Refilling.objects.all()
    drv = Driver.objects.all()
    vhc = Vehicle.objects.all()

    return render(request, 'refilling.html', {'refill': refill, 'driver': drv, 'vehicle': vhc, 'users': users})


def maintenance(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        Maintainance.objects.create(date=request.POST['date'], vehicle=request.POST['number'],
                                    driver=request.POST['driver'],
                                    mtype=request.POST['type'], description=request.POST['description'])
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
        return redirect('drivers:maintenance')
    else:
        tripss = Vehicle.objects.all()
        drvr = Driver.objects.all()
        return render(request, 'drmaintenance.html', {'vehicle': tripss, 'driver': drvr})
