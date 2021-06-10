from django.shortcuts import render, redirect
from staff.models import Request
from staff.forms import RequestForm
from django.http import HttpResponse


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
