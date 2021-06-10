from django.db import models
from staff.models import Request


# Create your models here.

class Assigned(models.Model):
    driver_id = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    staff_id = models.ForeignKey(Request, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.driver_id + ' - ' + str(self.status) + ' - ' + str(self.staff_id)


class Vehicle(models.Model):
    class Fuel(models.TextChoices):
        petrol = 'Petrol'
        diesel = 'Diesel'
        electric = 'Electric'
        hybrid = 'Hybrid'

    class Status(models.TextChoices):
        available = 'Available'
        onTrip = 'On Trip'
        garage = 'Garage'

    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50, choices=Fuel.choices, default=Fuel.petrol)
    maintenance_record = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.available)
    tank = models.CharField(max_length=50, default=80)
    last_refill = models.CharField(max_length=50)
    millaege = models.CharField(max_length=50, default=0)


class Inspection(models.Model):
    license_plate = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver_seat_belt = models.BooleanField(default=True)
    horn = models.BooleanField(default=True)
    steering = models.BooleanField(default=True)
    brakes = models.BooleanField(default=True)
    indicators = models.BooleanField(default=True)
    speedometer = models.BooleanField(default=True)
    wipers = models.BooleanField(default=True)
    body_interior = models.BooleanField(default=True)
    extinguisher = models.BooleanField(default=True)
    first_aid = models.BooleanField(default=True)
    floor_traps = models.BooleanField(default=True)
    hammers = models.BooleanField(default=True)
    emergency = models.BooleanField(default=True)
    passenger_door = models.BooleanField(default=True)
    mirrors = models.BooleanField(default=True)
    body_exterior = models.BooleanField(default=True)
    discs = models.BooleanField(default=True)
    glass = models.BooleanField(default=True)
    spare_wheel = models.BooleanField(default=True)
    tyres = models.BooleanField(default=True)
    engine_oil = models.BooleanField(default=True)
    engine_water = models.BooleanField(default=True)
    fuel = models.BooleanField(default=True)
    battery = models.BooleanField(default=True)
    exhaust = models.BooleanField(default=True)
    reflectors = models.BooleanField(default=True)
    lice_plate_condition = models.BooleanField(default=True)
    defect = models.TextField(max_length=255, blank=True)
    action = models.TextField(max_length=255, blank=True)
