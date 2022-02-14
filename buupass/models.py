from django.db import models
from decimal import Decimal

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
    bus_registration = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    bus_organisation = models.ForeignKey(BusOrganisation, related_name='bus', on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

        
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
