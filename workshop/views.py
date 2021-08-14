from django.shortcuts import render, redirect
from workshop.models import Maintainance
from workshop.forms import MaintenanceForm


# Create your views here.


def workshop(request):
    return render(request, 'workshop_index.html')


def pending(request):
    pen = Maintainance.objects.all()
    return render(request, 'pending.html', {'pend': pen})


def completed(request):
    com = Maintainance.objects.all()
    return render(request, 'completed.html', {'com': com})


def update_status(request, pending_id):
    if request.method == "POST":
        upd = Maintainance.objects.get(pk=pending_id)
        form = MaintenanceForm(request.POST or None, instance=upd)
        Maintainance.objects.filter(id=pending_id).update(status=request.POST['status'])
        if form.is_valid():
            form.save()
        return redirect('workshop:pending')
    else:
        upd_obj = Maintainance.objects.get(pk=pending_id)

        return render(request, 'editstatus.html', {'upd': upd_obj})


def major(request):
    maj = Maintainance.objects.all()
    return render(request, 'majormaintain.html', {'maj': maj})


def requests(request, request_id):
    return render(request, 'editmajor.html', {})
