from django.shortcuts import render

# Create your views here.


def workshop(request):
    return render(request, 'workshop_index.html')
