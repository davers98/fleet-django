from django.shortcuts import render


# Create your views here.

def human(request):
    return render(request, 'hr_index.html', {})
