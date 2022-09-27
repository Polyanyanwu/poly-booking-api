""" Urls for the API app """

from django.urls import path
from . import views


urlpatterns = [
    path('fcode', views.maintain_facility_code, name='maintain_facilities'),
]
