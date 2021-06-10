from django.http import HttpResponse
from django.shortcuts import render
from accounts.forms import UsersForm
from accounts.models import Users
from main.urls import urlpatterns


# Create your views here.
def account(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if request.user.is_authenticated:
            if Users.objects.values_list('transport' == True):
                return render(request, 'index.html', {})
            elif Users.objects.values_list('staff' == True):
                return render(request, 'staff_index.html', {})
            elif Users.objects.values_list('driver' == True):
                return render(request, 'driver_index.html', {})
            elif Users.objects.values_list('humanresource' == True):
                return render(request, 'hr_index.html', {})
            elif Users.objects.values_list('gpsa' == True):
                return render(request, 'gp_index.html', {})
            elif Users.objects.values_list('workshop' == True):
                return render(request, 'workshop_index.html', {})
        else:
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})
