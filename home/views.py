from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import HotelSerializer
from api.models import Hotel


def index(request):
    """ A view to return the index page """

    app_url = settings.APP_URL.strip()
    if 'search' in request.GET:
        criteria = request.GET['search']
        if not criteria:
            messages.error(request, "Please enter a search criteria\
                    before searching!")
            return redirect(reverse('home'))
        url = app_url + '/api/hotels?search=' + criteria

    else:
        url = app_url + '/api/hotels'
    response = requests.get(url)
    hotels = response

    if 'name' not in hotels.text:  # no hotel found
        messages.warning(request,
                         "No hotels matching your criteria, Please try again")
    if response.status_code == 200:
        try:
            hotels = response.json()
        except requests.exceptions.JSONDecodeError:
            messages.error(request,
                           "Could not retrieve hotels, Please try later")

    return render(request, 'home/index.html', {'hotels': hotels})


def hotel_details(request, hotel_id):

    url = settings.APP_URL + '/api/hotels/' + str(hotel_id) + "/"
    response = requests.get(url)
    hotels = None
    if response.status_code == 200:
        try:
            hotels = response.json()
        except requests.exceptions.JSONDecodeError:
            messages.error(request,
                           "Could not retrieve hotel, Please try later")
    hotel = None
    if hotels:
        hotel = hotels[0]
    return render(request, 'home/hotel_details.html',
                  {'hotel': hotel})
