from django.urls import path
from staff import views


urlpatterns = [
    path('', views.staff, name='staff'),
    # path('edit/<request_id>', views.edit_request, name='edit_request')
]
