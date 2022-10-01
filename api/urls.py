""" Urls for the API app """

from django.urls import path
from . import views


urlpatterns = [
    path('fcode', views.maintain_facility_code, name='maintain_facilities'),
    path('room_type', views.maintain_room_types, name='maintain_room_types'),
    path('hotels/<int:hotel_id>/', views.HotelDetailListApiView().as_view()),
    path('hotels', views.HotelListApiView().as_view()),
    path('hotel-room/<int:hotel_id>/', views.HotelRoomListApiView().as_view()),
    path('hotel-room/<int:hotel_id>/<int:room_id>/',
         views.HotelRoomDetailsApiView().as_view()),
    path('room-facility/<int:hotel_id>/<int:room_type_id>/',
         views.HotelRoomFacilityListApiView().as_view()),
    path('list_codes', views.list_codes, name='list_codes'),
]
