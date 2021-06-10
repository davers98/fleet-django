from django.urls import path
from workshop import views


urlpatterns = [
    path('', views.workshop, name='workshop')
]