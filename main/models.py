from django.db import models
from driver.models import Vehicle



# Create your models here.
class VehicleStatus(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Available')
    assigned = models.CharField(max_length=50)

    def __str__(self):
        return str(self.vehicle) + self.assigned + self.status



