from django.contrib import admin
from .models import Bus, BusOrganisation, Schedule, Route
# Register your models here.
admin.site.register(Bus)
admin.site.register(BusOrganisation)
admin.site.register(Schedule)
admin.site.register(Route)