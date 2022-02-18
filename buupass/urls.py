from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', views.home, name="home"),
    path('findbus/', cache_page(60*5)(views.FindBusView.as_view()), name="findbus"),
    path('seats/<int:pk>/', views.seats, name="seats"),
    # path('occupied/', views.occupiedSeats, name="occupied_seat")

    # path('bookings', views.bookings, name="bookings"),
    # path('cancellings', views.cancellings, name="cancellings"),
    # path('seebookings', views.seebookings, name="seebookings"),
    # path('signup', views.signup, name="signup"),
    # path('signin', views.signin, name="signin"),
    # path('success', views.success, name="success"),
    # path('signout', views.signout, name="signout"),

]
