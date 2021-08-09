from django.urls import path
from humanresource import views

app_name = "<hr>"

urlpatterns = [
    path('', views.human, name='human'),
    path('refilling requests', views.refill, name='refill'),
    path('refilling/edit/<request_id>', views.edit_request, name='edit_request'),
    path('maintenance', views.maintenance, name='maintenance')
]