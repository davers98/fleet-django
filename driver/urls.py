from django.urls import path
from driver import views


app_name = '<drivers>'

urlpatterns = [
    path('', views.driver, name='driver'),
    path('trip/', views.trip, name='trip')
]
