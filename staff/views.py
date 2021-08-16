from django.http import HttpResponse
from django.shortcuts import render, redirect
from staff.models import Request
from staff.forms import RequestForm
from accounts.decorators import staff_required


# Create your views here.


def staff(request):
    if request.method == "POST":

        form = RequestForm(request.POST)
        print(form)
        Request.objects.create(staff_id=request.POST['staffid'], purpose=request.POST['purpose'],
                               trip_date=request.POST['date'],
                               time=request.POST['time'], department=request.POST['department'],
                               destination=request.POST['destination'])
        if form.is_valid():
            form.save()
        return redirect('staff')
    else:
        tripss = Request.objects.all()
    return render(request, 'staff_index.html', {'trips': tripss})


def staff_request(request):
    if request.method == "POST":

        form = RequestForm(request.POST)
        print(form)
        Request.objects.create(staff_id=request.POST['staffid'], purpose=request.POST['purpose'],
                               trip_date=request.POST['date'], contact=request.POST['contact'],
                               time=request.POST['time'], department=request.POST['department'],
                               destination=request.POST['destination'])
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
        return redirect('staff:staff_request')
    else:
        tripss = Request.objects.all()
        return render(request, 'staff_request.html', {'trips': tripss})


def history(request):
    tripss = Request.objects.all()
    return render(request, 'history.html', {'trips': tripss})


def reqCom(request, status_id):
    if request.method == "POST":

        stat = Request.objects.get(pk=status_id)
        form = RequestForm(request.POST or None, instance=stat)
        Request.objects.filter(id=status_id).update(trip_status=request.POST['status'])
        if form.is_valid():
            form.save()
        return redirect('staff:staff')
    else:
        stat_obj = Request.objects.get(pk=status_id)
        print(status_id)
        return render(request, 'requComp.html', {'stat': stat_obj})
