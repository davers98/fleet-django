from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from accounts.forms import LoginForm
from django.contrib.auth import get_user_model
from accounts.models import User
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy


# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                type_obj = User.objects.get(username=user)

                if user.is_authenticated and type_obj.user_type == 1:
                    return HttpResponseRedirect(reverse_lazy('main:transport'))

                elif user.is_authenticated and type_obj.user_type == 2:
                    return HttpResponseRedirect(reverse_lazy('drivers:driver'))

                elif User.user_type == 3:
                    return render(request, 'hr_index.html', {})

                elif user.is_authenticated and type_obj.user_type == 4:
                    return HttpResponseRedirect(reverse_lazy('staff:staff'))
            else:
                messages.error(request, "Account is Disabled")
        else:
            messages.error(request, 'Wrong Email and Username')
    else:
        form = LoginForm()

    return render(request, 'login.html', {})
