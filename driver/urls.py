from django.urls import path
from driver import views


app_name = '<drivers>'

urlpatterns = [
    path('', views.driver, name='driver'),
    path('trip/', views.trip, name='trip'),
    path('inspection/', views.inspection, name='inspection'),
    path('refilling/', views.refilling, name='refilling'),
    path('maintenance/', views.maintenance, name='maintenance')
]
