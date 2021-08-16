from django.shortcuts import render, redirect
from staff.models import Request
from staff.forms import RequestForm
from driver.models import Refilling, Vehicle, Driver, Locations
from workshop.models import Maintainance, MajorMaintainance
from accounts.models import User
from main.models import VehicleStatus
from driver.forms import RefillingForm
from workshop.forms import MaintenanceForm
from accounts.decorators import transport_required
from django.http import HttpResponse
from main.forms import VehicleForm, DriverForm
from django.core.mail import send_mail
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import random


# Create your views here.

def transport(request):
    mapbox_access_token = 'pk.eyJ1IjoiaWRhdmVyczk4IiwiYSI6ImNrcXBzZWxmczA4Mm8ydnEzMXR3emt3eXcifQ.d-QVNcLt_5acuWmgUpBPTA'
    return render(request, 'index.html', {'mapbox_access_token': mapbox_access_token})


def requests(request):
    tripss = Request.objects.all()
    return render(request, 'request.html', {'trips': tripss})


def edit_request(request, request_id):
    if request.method == "POST":

        req = Request.objects.get(pk=request_id)
        form = RequestForm(request.POST or None, instance=req)
        # Request.objects.update(driver=request.POST['driver'])
        Request.objects.filter(id=request_id).update(driver=request.POST['driver'], approved_by=request.POST['trans'])
        sms = request.POST['driver']
        number = Request.objects.raw('select phone from driver_assigned')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            send_mail(
                'Trip FeedBack',
                'Your Trip information is already posted login to check status',
                'davidrobert785@gmail.com',
                ['davidrobert10@ymail.com'],
                fail_silently=False
            )

        return redirect('main:requests')
    else:
        req_obj = Request.objects.get(pk=request_id)
        drv = Driver.objects.all()
        users = User.objects.all()
        print(request_id)
        return render(request, 'edit.html', {'req_obj': req_obj, 'driver': drv, 'users': users})


def status(request):
    if request.method == "POST":

        form = VehicleForm(request.POST)
        print(form)
        Vehicle.objects.create(model=request.POST['vmodel'], license=request.POST['licence'],
                               fuel_type=request.POST['fuel'],
                               manufacturer=request.POST['make'], color=request.POST['vcolor'],
                               transmission=request.POST['trans'], seats=request.POST['vseat'],
                               status=request.POST['status'],
                               body=request.POST['type'], last_refill=request.POST['refill'],
                               maintenance_record=request.POST['vmaint'],
                               operability=request.POST['op'], mileage=request.POST['milleage'])
        if form.is_valid():
            form.save()
        return redirect('main:status')
    else:
        tripss = Vehicle.objects.all()
        loc = [Locations.objects.all().last()]

        # last_date = loc.id
        return render(request, 'vehStatus.html', {'trips': tripss, 'loc': loc})


def edit_status(request, status_id):
    if request.method == "POST":

        stat = VehicleStatus.objects.get(pk=status_id)
        form = VehicleForm(request.POST or None, instance=stat)
        VehicleStatus.objects.filter(id=status_id).update(status=request.POST['status'])
        if form.is_valid():
            form.save()
        return redirect('main:status')
    else:
        stat_obj = VehicleStatus.objects.get(pk=status_id)
        print(status_id)
        return render(request, 'edit_status.html', {'stat': stat_obj})


def filling(request):
    tripss = Refilling.objects.all()
    return render(request, 'filling requests.html', {'trips': tripss})


def edit_filling(request, filling_id):
    if request.method == "POST":
        fill = Refilling.objects.get(pk=filling_id)
        form = RefillingForm(request.POST or None, instance=fill)
        Refilling.objects.filter(id=filling_id).update(number=request.POST['namba'], approved=request.POST['transport'])
        if form.is_valid():
            instance = form.save(commit=False)
            instance.received_by = request.user
        return redirect('main:filling')
    else:
        fill_obj = Refilling.objects.get(pk=filling_id)
        tro = User.objects.all()
        number = random.randint(1, 798)
        return render(request, 'edit_filling.html', {'fill': fill_obj, 'num': number, 'users': tro})


def driver(request):

    if request.method == 'POST':
        form = DriverForm(request.POST or None, request.FILES or None)

        Driver.objects.create(driver_name=request.POST['fname'],
                              vehicle=request.POST['number'], status=request.POST['status'],
                              phone=request.POST['phone'], added_by=request.POST['added_by'])
        if form.is_valid():
            form.save()

        return redirect('main:driver')
    else:
        tripss = Driver.objects.all()

        vehicle = Vehicle.objects.all()

        users = User.objects.all()
        return render(request, 'driver.html', {'trips': tripss, 'vehicle': vehicle, 'users': users})


def maintenance(request):
    main = Maintainance.objects.all()
    return render(request, 'maintenance.html', {'main': main})


def edit_main(request, main_id):
    if request.method == "POST":
        main = Maintainance.objects.get(pk=main_id)
        form = MaintenanceForm(request.POST or None, instance=main)
        Maintainance.objects.filter(id=main_id).update(transport=request.POST['transport'])
        if form.is_valid():
            form.save()
        return redirect('main:maintenance')
    else:
        main_obj = Maintainance.objects.get(pk=main_id)
        tro = User.objects.all()
        # number = random.randint(1, 798)
        return render(request, 'editmain.html', {'main': main_obj, 'user': tro})


def assign(request, driver_id):
    if request.method == "POST":
        drv = Driver.objects.get(pk=driver_id)
        form = DriverForm(request.POST or None, instance=drv)
        Driver.objects.filter(id=driver_id).update(vehicle=request.POST['vehicle'])
        if form.is_valid():
            form.save()
        return redirect('main:driver')
    else:
        drv_obj = Driver.objects.get(pk=driver_id)
        veh = Vehicle.objects.all()
        tro = User.objects.all()
        # number = random.randint(1, 798)
        return render(request, 'assign.html', {'drv': drv_obj, 'user': tro, 'veh': veh})


def aval(request, set_id):
    if request.method == "POST":
        drv = Driver.objects.get(pk=set_id)
        form = DriverForm(request.POST or None, instance=drv)
        Driver.objects.filter(id=set_id).update(status=request.POST['status'])
        if form.is_valid():
            form.save()
        return redirect('main:driver')
    else:
        drv_obj = Driver.objects.get(pk=set_id)
        veh = Vehicle.objects.all()
        tro = User.objects.all()
        # number = random.randint(1, 798)
        return render(request, 'setAvailable.html', {'drv': drv_obj, 'user': tro, 'veh': veh})


def delete_drv(request, driver_id):
    drv = Driver.objects.get(pk=driver_id)
    drv.delete()
    return redirect('main:driver')