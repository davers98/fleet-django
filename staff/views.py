from django.http import HttpResponse
from django.shortcuts import render, redirect
from staff.models import Request
from staff.forms import RequestForm
from accounts.decorators import staff_required


# Create your views here.


@staff_required
def staff(request):
    # if request.method == "POST":
    #
    #     form = RequestForm(request.POST)
    #     print(form)
    #     Request.objects.create(staff_id=request.POST['staffid'], trip_details=request.POST['tripdetails'],
    #                            trip_time=request.POST['triptime'])
    #     if form.is_valid():
    #         form.save()
    #     return redirect('staff')
    # else:
    tripss = Request.objects.all()
    return render(request, 'staff_index.html', {'trips': tripss})


def staff_request(request):
    if request.method == "POST":

        form = RequestForm(request.POST)
        print(form)
        Request.objects.create(staff_id=request.POST['staffid'], trip_details=request.POST['tripdetails'],
                               trip_time=request.POST['triptime'])
        if form.is_valid():
            form.save()
        return redirect('staff:staff_request')
    else:
        tripss = Request.objects.all()
        return render(request, 'staff_request.html', {'trips': tripss})
