from django.urls import path
from gpsa import views

urlpatterns = [
    path('', views.gpsa, name='gpsa'),
]