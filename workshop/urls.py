from django.urls import path
from workshop import views

app_name = '<workshop>'

urlpatterns = [
    path('', views.workshop, name='workshop'),
    path('Pending Maintenance/', views.pending, name='pending'),
    path('Completed Maintenance/', views.completed, name='completed'),
    path('Pending Maintenance/edit/<pending_id>', views.update_status, name='update_status')

]