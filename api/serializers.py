# api/serializers.py
from rest_framework import serializers
from buupass import models


class BusOrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'logo',
        )
        model = models.BusOrganisation

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'departure_location',
            'destination_location',
        )
        model = models.Route


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'bus_registration',
            'description',
            'bus_organisation',
            'capacity',
            'route',
        )
        model = models.Bus

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'departure_time',
            'arrival_time',
            'bus',
            'price',
            'route',
        )
        model = models.Schedule
