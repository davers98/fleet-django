from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

app_name = '<main>'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='account')
]
