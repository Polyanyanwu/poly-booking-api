""" URL Configuration for home app """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('<int:hotel_id>/', views.hotel_details, name='hotel_details'),
]
