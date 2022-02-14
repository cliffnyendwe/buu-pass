# api/urls.py
from django.urls import path, include

from . import views

urlpatterns = [
    path('organisations/', views.ListBusOrganisation.as_view()),
    path('organisation/<int:pk>/', views.DetailBusOrganisation.as_view()),

    path('routes/', views.ListRoute.as_view()),
    path('route/<int:pk>/', views.DetailRoute.as_view()),

    path('buses/', views.ListBus.as_view()),
    path('bus/<int:pk>/', views.DetailBus.as_view()),

    path('schedules/', views.ListSchedule.as_view()),
    path('schedule/<int:pk>/', views.DetailSchedule.as_view()),

    # path('rest-auth/', include('rest_auth.urls')),
]
