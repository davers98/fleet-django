from django.contrib import admin
from driver.models import Driver, Vehicle, Inspection, Refilling, RandomRefill, Maintainance

# Register your models here.
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(Inspection)
admin.site.register(Refilling)
admin.site.register(RandomRefill)
admin.site.register(Maintainance)