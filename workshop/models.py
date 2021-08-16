from django.db import models
from accounts.models import User


# Create your models here.

class Maintainance(models.Model):
    class Status(models.TextChoices):
        planned = 'Planned'
        nonplanned = 'Non-Planned'

    vehicle = models.CharField(max_length=50)
    driver = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    mtype = models.CharField(max_length=50, )
    date = models.CharField(max_length=50, blank=True)
    transport = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=50, blank=True)
    # user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)


class MajorMaintainance(models.Model):
    class Status(models.TextChoices):
        approved = 'Approved'
        pending = 'Pending'

    vehicle = models.CharField(max_length=50)
    spare = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.pending)
    human = models.CharField(max_length=50)
    # user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
