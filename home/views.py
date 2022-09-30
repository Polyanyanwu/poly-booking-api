from django.shortcuts import render
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import HotelSerializer
from api.models import Hotel
# Create your views here.


@api_view(['GET'])
def get_hotels(request):
    """ A view to return the hotels """
    if request.method == 'GET':
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)


def index(request):
    """ A view to return the index page """

    # if request.method == 'GET':
    #     hotels = get_hotels(request)
    #     print("hotels==", hotels.data)

    app_url = settings.APP_URL.strip()
    response = requests.get(app_url + '/api/hotels')

    if response.status_code == 200:
        response = response.json()
        # print(hotels)
    home_msg = response
    print("response==", response)
    return render(request, 'home/index.html', {'msg': home_msg})
