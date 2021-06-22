from django.db import models
from staff.models import Request


# Create your models here.

class Assigned(models.Model):
    driver_id = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    staff_id = models.CharField(max_length=50)

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
    license_plate = models.CharField(max_length=50, unique=True)
    fuel_type = models.CharField(max_length=50, choices=Fuel.choices, default=Fuel.petrol)
    maintenance_record = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.available)
    tank = models.CharField(max_length=50, default=80)
    last_refill = models.CharField(max_length=50)
    mileage = models.CharField(max_length=50, default=0)

    def __str__(self):
        return (self.manufacturer + ' - ' + str(
            self.model) + ' - ' + self.license_plate + ' - ' + self.fuel_type + ' - ' + self.maintenance_record
                + ' - ' + self.status + ' - ' + self.tank + ' - ' + self.last_refill + ' - ' + self.mileage)


class Inspection(models.Model):
    license_plate = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    driver_seat = models.CharField(max_length=50)
    horn = models.CharField(max_length=50)
    steering = models.CharField(max_length=50)
    brakes = models.CharField(max_length=50)
    indicators = models.CharField(max_length=50)
    speedometer = models.CharField(max_length=50)
    wipers = models.CharField(max_length=50)
    body_interior = models.CharField(max_length=50)
    extinguisher = models.CharField(max_length=50)
    first_aid = models.CharField(max_length=50)
    floor_traps = models.CharField(max_length=50)
    # hammers = models.CharField(max_length=50)
    emergency = models.CharField(max_length=50)
    passenger_door = models.CharField(max_length=50)
    mirrors = models.CharField(max_length=50)
    body_exterior = models.CharField(max_length=50)
    discs = models.CharField(max_length=50)
    inflation = models.CharField(max_length=50)
    spare_wheel = models.CharField(max_length=50)
    fixing = models.CharField(max_length=50)
    engine = models.CharField(max_length=50)
    # engine_water = models.CharField(max_length=50)
    # fuel = models.CharField(max_length=50)
    battery = models.CharField(max_length=50)
    exhaust = models.CharField(max_length=50)
    reflectors = models.CharField(max_length=50)
    lice_plate_condition = models.CharField(max_length=50)
    defect = models.TextField(max_length=255, blank=True)
    action = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return (
                self.driver_seat_belt + self.horn + self.steering + self.brakes + self.indicators + self.speedometer +
                self.wipers + self.body_exterior + self.extinguisher + self.first_aid + self.floor_traps + self.hammers
                + self.emergency + self.passenger_door
                + self.mirrors + self.body_exterior + self.discs + self.glass + self.glass + self.spare_wheel
                + self.tyres + self.engine_oil + self.engine_water + self.fuel + self.battery
                + self.exhaust + self.reflectors + self.lice_plate_condition + int(self.defect) + int(self.action))
