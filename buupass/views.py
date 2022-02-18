import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Schedule, Route, Seat
from django.views.decorators.cache import cache_page
from django.views.generic import View, CreateView

# Create your views here.
def home(request):
    schedules = Schedule.objects.all()
    return render(request, 'index.html')

class FindBusView(CreateView):
    template_name = 'findbus.html'
    def post(self,request):
        context = {}
        source_r = request.POST.get('source')
        dest_r = request.POST.get('destination')
        date_r = request.POST.get('date')
        route = Route.objects.filter(departure_location=source_r, destination_location = dest_r).first()
        bus_list = Schedule.objects.filter(route=route, departure_time=date_r)
        if bus_list:
            return render(request, 'list.html', locals())
        else:
            context["error"] = "Sorry no buses availiable"
            return render(request, 'findbus.html', context)


@cache_page(60*5)
def seats(request, pk):
    schedule = Schedule.objects.get(pk=pk)
    layout = schedule.bus.layout
    seats =Seat.objects.filter(bus=schedule.bus.pk)
    if layout=='3-2':
        i = 5
    else:
        i = 4
    return render(request,'select_seat.html', locals())

# @cache_page(60*5)
# def occupiedSeats(request):
#     data = json.loads(request.body)
#     print(data)
#     schedule = Schedule.objects.get(pk=data["schedule_pk"])
#     occupied = schedule.bus.booked_seats.all()
#     occupied_seat = list(map(lambda seat: seat.id, occupied))

#     return JsonResponse (
#         {
#             "occupied_seats":occupied_seat,
#             "schedule": str(schedule)
#         }
#     )
        
