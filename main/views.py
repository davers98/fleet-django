from django.shortcuts import render, redirect
from staff.models import Request
from staff.forms import RequestForm
from main.models import VehicleStatus
from accounts.decorators import transport_required
from django.http import HttpResponse
from main.forms import VehicleForm


# Create your views here.

def transport(request):
    return render(request, 'index.html', {})


def requests(request):
    tripss = Request.objects.all()
    return render(request, 'request.html', {'trips': tripss})


def edit_request(request, request_id):
    if request.method == "POST":

        req = Request.objects.get(pk=request_id)
        form = RequestForm(request.POST or None, instance=req)
        # Request.objects.update(driver=request.POST['driver'])
        Request.objects.filter(id=request_id).update(driver=request.POST['driver'])
        if form.is_valid():
            form.save()

        return redirect('main:requests')
    else:
        req_obj = Request.objects.get(pk=request_id)
        print(request_id)
        return render(request, 'edit.html', {'req_obj': req_obj})


def status(request):
    if request.method == "POST":

        form = VehicleForm(request.POST)
        print(form)
        # VehicleStatus.objects.create(vehicle=request.POST['vehicle'], status=request.POST['status'],
        #                              assigned=request.POST['assigned'])
        if form.is_valid():
            form.save()
        return redirect('main:status')
    else:
        tripss = VehicleStatus.objects.all()
        return render(request, 'vehStatus.html', {'trips': tripss})


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


# def vehicle_status(request, status_id):

