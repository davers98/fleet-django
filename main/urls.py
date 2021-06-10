from django.urls import path, include
from main import views
from staff.models import Request


app_name = "<main>"

urlpatterns = [
    # path('', include(('main.urls', 'main'), namespace='main')),
    path('', views.transport, name='transport'),
    path('requests', views.requests, name='requests'),
    path('requests/edit/<request_id>', views.edit_request, name='edit_request')
]
