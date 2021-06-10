from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('transport/', include('main.urls', namespace='main')),
    path('driver/', include('driver.urls', namespace='drivers')),
    path('hr/', include('humanresource.urls', namespace='hr')),
    path('gpsa/', include('gpsa.urls')),
    path('staff/', include('staff.urls')),
    path('workshop/', include('workshop.urls')),

]
