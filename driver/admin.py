from django.contrib import admin
from driver.models import Assigned, Vehicle, Inspection

# Register your models here.
admin.site.register(Assigned)
admin.site.register(Vehicle)
admin.site.register(Inspection)