from django.db import models
from driver.models import Vehicle


# Create your models here.
class VehicleStatus(models.Model):
    vehicle = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='Available')
    assigned = models.CharField(max_length=50)

    def __str__(self):
        return self.status + self.assigned + self.status
