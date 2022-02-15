from django.db import models
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class BusOrganisation(models.Model):
    '''
    Class to define a bus company
    '''
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="logo-pic/", blank=True) 

    def __str__(self):
        return self.name


class Route(models.Model):
    departure_location = models.CharField(max_length=255)
    destination_location = models.CharField(max_length=255)

    def __str__(self):
        return self.departure_location +" >> "+ self.destination_location


class Bus(models.Model):
    TWOBYTWO = '2-2'
    THREEBYTWO = '3-2'
    bus_registration = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    bus_organisation = models.ForeignKey(BusOrganisation, related_name='bus', on_delete=models.CASCADE)

    capacity = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(67), MinValueValidator(14)])
    available = models.DecimalField(decimal_places=0, max_digits=2)
    layout  = ((TWOBYTWO,'Two By Two'), (THREEBYTWO, 'Three By Two'))

    def __str__(self):
        return self.bus_registration

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email


class Schedule(models.Model):
    '''
    Class to define a bus schedule
    '''
    departure_time = models.DateTimeField(auto_now_add=False)
    arrival_time = models.DateTimeField(auto_now_add=False)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15 ,decimal_places=2, default=Decimal(0.00))
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __str__(self):
        return self.bus.bus_organisation.name + ' Bus No.' + str(self.bus.id) + ' Schedule No.' + str(self.id)

class Booking(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)

