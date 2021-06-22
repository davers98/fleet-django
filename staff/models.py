from django.db import models


# Create your models here.


class Request(models.Model):
    staff_id = models.CharField(max_length=100)
    trip_details = models.TextField()
    trip_time = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    driver = models.CharField(max_length=50, blank=True, default='Not Assigned')

    def __str__(self):
        return self.staff_id + " - " + self.trip_details + " - " + str(self.trip_time) + " - " + str(self.date)


