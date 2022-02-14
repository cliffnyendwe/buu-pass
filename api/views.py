from rest_framework import generics
from buupass import models
from . import serializers


class ListBusOrganisation(generics.ListCreateAPIView):
    queryset = models.BusOrganisation.objects.all()
    serializer_class = serializers.BusOrganisationSerializer


class DetailBusOrganisation(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BusOrganisation.objects.all()
    serializer_class = serializers.BusOrganisationSerializer


class ListRoute(generics.ListCreateAPIView):
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer


class DetailRoute(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer



class ListBus(generics.ListCreateAPIView):
    queryset = models.Bus.objects.all()
    serializer_class = serializers.BusSerializer


class DetailBus(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Bus.objects.all()
    serializer_class = serializers.BusSerializer




class ListSchedule(generics.ListCreateAPIView):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer


class DetailSchedule(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer

                                