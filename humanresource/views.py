from django.shortcuts import render, redirect
from driver.models import Refilling
from driver.forms import RefillingForm


# Create your views here.

def human(request):
    return render(request, 'hr_index.html', {})


def refill(request):
    ref = Refilling.objects.all()
    return render(request, 'fill requests.html', {'ref': ref})


def edit_request(request, request_id):
    if request.method == "POST":
        req = Refilling.objects.get(pk=request_id)
        form = RefillingForm(request.POST or None, instance=req)
        Refilling.objects.filter(id=request_id).update(status=request.POST['status'])
        if form.is_valid():
            instance = form.save(commit=False)
            instance.hr = request.user
        return redirect('hr:refill')
    else:
        ref = Refilling.objects.get(pk=request_id)
        return render(request, 'edit_request.html', {'ref': ref})


def maintenance(request):
    return render(request, 'basehr.html', {})