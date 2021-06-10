from django.shortcuts import render


# Create your views here.

def gpsa(request):
    return render(request, 'gp_index.html')
