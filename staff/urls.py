from django.urls import path
from staff import views


app_name = '<staff>'

urlpatterns = [
    path('', views.staff, name='staff'),
    # path('edit/<request_id>', views.edit_request, name='edit_request')
    path('request', views.staff_request, name='staff_request'),
    path('History', views.history, name='history'),
    path('request/Request Status/<status_id>', views.reqCom, name='reqCom'),
]
