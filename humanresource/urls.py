from django.urls import path
from humanresource import views

app_name = "<hr>"

urlpatterns = [
    path('', views.human, name='human'),
]