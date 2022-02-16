from django.contrib import admin
from .models import Bus, BusOrganisation, Schedule, Route,Seat
# Register your models here.
admin.site.register(Bus)
admin.site.register(BusOrganisation)
admin.site.register(Schedule)
admin.site.register(Route)
admin.site.register(Seat)