from django.urls import path, include
from main import views
from staff.models import Request


app_name = "<main>"

urlpatterns = [
    # path('', include(('main.urls', 'main'), namespace='main')),
    path('', views.transport, name='transport'),
    path('requests', views.requests, name='requests'),
    path('requests/edit/<request_id>', views.edit_request, name='edit_request'),
    path('Vehicle Status/', views.status, name='status'),
    path('Vehicle Status/edit/<status_id>', views.edit_status, name='edit_status'),
    path('Filling Requests/', views.filling, name='filling'),
    path('Filling Requests/edit/<filling_id>', views.edit_filling, name='edit_filling'),
    path('drivers/', views.driver, name='driver'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('maintenance/edit/<main_id>', views.edit_main, name='edit_main'),
    path('Driver/Assign/edit/<driver_id>', views.assign, name='assign'),
    path('Driver/Set Status/edit/<set_id>', views.aval, name='aval'),
    path('delete/<driver_id>', views.delete_drv, name='delete_drv'),
]
