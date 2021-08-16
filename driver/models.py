from django.db import models
from staff.models import Request
from accounts.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from random import randint


# Create your models here.


class Driver(models.Model):
    # driver_id = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=50, default='david')
    vehicle = models.CharField(max_length=50, blank=True, default='Not Assigned')
    status = models.CharField(max_length=50)
    staff_id = models.CharField(max_length=50, blank=True, default='Not Assigned')
    phone = models.CharField(max_length=50, default='+255716228159')
    added_by = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.driver_id + ' - ' + str(self.status) + ' - ' + str(self.staff_id) + ' - ' + self.phone


class Vehicle(models.Model):
    class Fuel(models.TextChoices):
        petrol = 'Petrol'
        diesel = 'Diesel'
        electric = 'Electric'
        hybrid = 'Hybrid'

    class Status(models.TextChoices):
        available = 'Available'
        unavailable = 'Unavailable'

    class Trans(models.TextChoices):
        manual = 'Manual'
        auto = 'Auto'

    class Operability(models.TextChoices):
        operable = 'Operable'
        inoperable = 'Inoperable'

    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    license = models.CharField(max_length=50, unique=True)
    fuel_type = models.CharField(max_length=50, choices=Fuel.choices, default=Fuel.petrol)
    year = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50, choices=Trans.choices, default=Trans.auto)
    color = models.CharField(max_length=50)
    seats = models.CharField(max_length=50)
    body = models.CharField(max_length=50)
    operability = models.CharField(max_length=50, choices=Operability.choices, default=Operability.operable)
    maintenance_record = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.available)
    tank = models.CharField(max_length=50, default=80)
    last_refill = models.CharField(max_length=50)
    mileage = models.CharField(max_length=50, default=0)


    # user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return (self.manufacturer + ' - ' + str(
            self.model) + ' - ' + self.license + ' - ' + self.fuel_type + ' - ' + self.maintenance_record
                + ' - ' + self.status + ' - ' + self.tank + ' - ' + self.last_refill + ' - ' + self.mileage + ' - ' + self.year
                + ' - ' + self.operability + ' - ' + self.seats + ' - ' + self.year)


class Inspection(models.Model):
    license = models.CharField(max_length=50)
    driver = models.CharField(max_length=50, default='User')
    date = models.CharField(max_length=50, blank=True)
    odometer = models.CharField(max_length=100, default=0)
    # user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    defect = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return (
                self.driver_seat + self.horn + self.steering + self.brakes + self.indicators + self.speedometer +
                self.wipers + self.body_exterior + self.extinguisher + self.first_aid + self.floor_traps
                + self.emergency + self.passenger_door
                + self.mirrors + self.body_exterior + self.discs + self.spare_wheel
                + self.inflation + self.engine + self.fixing + self.battery
                + self.exhaust + self.reflectors + self.lice_plate_condition + str(self.defect) + str(self.action))


class Refilling(models.Model):
    class Status(models.TextChoices):
        approved = 'Approved'
        pending = 'Pending'

    driver = models.CharField(max_length=50)
    number = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now=True)
    towards = models.CharField(max_length=60)
    fuel = models.CharField(max_length=60)
    liters = models.CharField(max_length=60)
    vehicle = models.CharField(max_length=50)
    approved = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=60, choices=Status.choices, default=Status.pending)

    def __str__(self):
        return self.number + str(self.date) + self.fuel + self.liters + str(self.vehicle)


class RandomRefill(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)

    @staticmethod
    def radrefill():
        return str(randint(0, 2207))

    @receiver(post_save, sender=User)
    def create_latest_inputs(sender, instance, created, **kwargs):
        if created:
            RandomRefill.objects.create(user=instance)


class Locations(models.Model):
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.id + int(self.latitude) + int(self.longitude)
