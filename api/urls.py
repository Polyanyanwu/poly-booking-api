""" Urls for the API app """

from django.urls import path
from . import views


urlpatterns = [
    path('fcode', views.maintain_facility_code, name='maintain_facilities'),
    path('room_type', views.maintain_room_types, name='maintain_room_types'),
    path('hotels', views.HotelListApiView().as_view()),
]
