from django.db import models
from accounts.models import User


# Create your models here.


class Request(models.Model):
    staff_id = models.CharField(max_length=100)
    department = models.CharField(max_length=50, default='CCT')
    destination = models.CharField(max_length=50, default='POSTA')
    contact = models.CharField(max_length=50, default='0712345678')
    purpose = models.TextField()
    trip_date = models.CharField(max_length=50)
    time = models.CharField(max_length=50, default='12:00')
    date = models.DateTimeField(auto_now=True)
    driver = models.CharField(max_length=50, blank=True, default='Not Assigned')
    approved_by = models.CharField(max_length=50, blank=True, default='Not Approved')
    trip_status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return (self.staff_id + " - " + self.purpose + " - " + str(self.time) + " - " + " - " + str(self.department)
                + " - " + str(self.contact))
