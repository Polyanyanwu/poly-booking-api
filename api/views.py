""" Views for the api functions """

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db import transaction
from django.db.models import Q
from django.core.paginator import Paginator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from api.serializers import \
    (HotelSerializer, HotelRoomSerializer,
     RoomTypeSerializer, GeneralFacilitySerializer, FacilityCodeSerializer)
from .models import FacilityCode, RoomType, Hotel, HotelRoom, HotelRoomFacility
from .forms import FacilityCodeForm, RoomTypeForm


@login_required
@transaction.atomic
def maintain_facility_code(request):
    """ Maintain Facility Codes """
    # check that user is staff

    if not request.user.is_staff:
        messages.error(request,
                       "You are not authorized to perform this transaction")
        return redirect('/')

    facilities = FacilityCode.objects.all().order_by('name')
    use_instance = True
    if facilities.count() == 0:
        use_instance = False
        form = FacilityCodeForm()
    if request.method == 'POST':
        if 'edit' in request.POST:
            id_sent = request.POST.get('edit')
            facility = get_object_or_404(FacilityCode, id=id_sent)
            form = FacilityCodeForm(instance=facility)
            request.session['current_rec'] = id_sent
        elif 'create_new_record' in request.POST:
            form = FacilityCodeForm()
            request.session['current_rec'] = ""
        elif 'cancel_ops' in request.POST:
            if use_instance:
                form = FacilityCodeForm(instance=facilities[0])
                request.session['current_rec'] = facilities[0].id
            HttpResponseRedirect('api/facility_code.html')
        elif 'confirm-action-btn' in request.POST:
            # action is only delete action
            id_sent = request.POST.get('confirm-id')
            facility = get_object_or_404(FacilityCode, id=id_sent)
            name = facility.name
            facility.delete()
            request.session['current_rec'] = ""
            messages.success(request,
                             ('Facility ' + name +
                              ' was successfully deleted!'))
            if facilities.count():
                form = FacilityCodeForm(instance=facilities[0])
        elif 'save_record' in request.POST:

            if request.session.get('current_rec'):
                # editing a record which id was put in session
                facility_id = int(request.session.get('current_rec'))
                facility = FacilityCode.objects.get(pk=facility_id)
                form = FacilityCodeForm(request.POST, instance=facility)
            else:
                form = FacilityCodeForm(request.POST)
            if form.is_valid():
                new_rec = form.save()
                # put the newly saved record in edit mood to prevent
                # creating a new record again if the save key is pressed twice
                request.session['current_rec'] = new_rec.id
                messages.success(request,
                                 ('Your Facility was successfully saved!'))
            else:
                messages.error(request, ('Please correct the error below.'))
    else:
        if facilities.count():
            form = FacilityCodeForm(instance=facilities[0])
    paginator = Paginator(facilities, 10)  # Show 10 records
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'api/facility_code.html', {
        'form': form,
        'facilities': page_obj,
    })


@login_required
@transaction.atomic
def maintain_room_types(request):
    """ Maintain Room type Codes """
    # check that user is staff

    if not request.user.is_staff:
        messages.error(request,
                       "You are not authorized to perform this transaction")
        return redirect('/')

    room_types = RoomType.objects.all().order_by('name')
    use_instance = True
    if room_types.count() == 0:
        use_instance = False
        form = RoomTypeForm()
        request.session['current_rec'] = ""
    if request.method == 'POST':
        print(request.POST)
        if 'edit' in request.POST:
            id_sent = request.POST.get('edit')
            room_type = get_object_or_404(RoomType, id=id_sent)
            form = RoomTypeForm(instance=room_type)
            request.session['current_rec'] = id_sent
        elif 'create_new_record' in request.POST:
            form = RoomTypeForm()
            request.session['current_rec'] = ""
        elif 'cancel_ops' in request.POST:
            if use_instance:
                form = RoomTypeForm(instance=room_types[0])
                request.session['current_rec'] = room_types[0].id
            HttpResponseRedirect('api/room_type.html')
        elif 'confirm-action-btn' in request.POST:
            # action is only delete action
            id_sent = request.POST.get('confirm-id')
            room_type = get_object_or_404(RoomType, id=id_sent)
            name = room_type.name
            room_type.delete()
            request.session['current_rec'] = ""
            messages.success(request,
                             ('Room type: ' + name +
                              ' was successfully deleted!'))
            if room_types.count():
                form = RoomTypeForm(instance=room_types[0])
        elif 'save_record' in request.POST:

            if request.session.get('current_rec'):
                # editing a record which id was put in session
                room_type_id = int(request.session.get('current_rec'))
                room_type = RoomType.objects.get(pk=room_type_id)
                form = RoomTypeForm(request.POST, instance=room_type)
            else:
                form = RoomTypeForm(request.POST)
            if form.is_valid():
                new_rec = form.save()
                # put the newly saved record in edit mood to prevent
                # creating a new record again if the save key is pressed twice
                request.session['current_rec'] = new_rec.id
                messages.success(request,
                                 ('Your Room Type was successfully saved!'))
            else:
                messages.error(request, ('Please correct the error below.'))
    else:
        if room_types.count():
            form = RoomTypeForm(instance=room_types[0])
    paginator = Paginator(room_types, 10)  # Show 10 records
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'api/room_type.html', {
        'form': form,
        'room_types': page_obj,
    })


def list_codes(request):
    room_types = RoomType.objects.all().order_by('name')
    facility_codes = FacilityCode.objects.all().order_by('name')

    return render(request, 'api/codes_list.html', {
        'room_types': room_types,
        'facility_codes': facility_codes,
    })


class HotelListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all Hotels
    def get(self, request, *args, **kwargs):
        '''
        List all the hotel rooms for given requested user
        '''
        hotels = Hotel.objects.all()
        # print("request get==", request.GET)
        if 'search' in request.GET:
            criteria = request.GET['search']
            if criteria:
                hotels = hotels.filter(
                    (Q(name__icontains=criteria) | Q(
                        city__icontains=criteria)))
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the Hotel with given data
        include hotel rooms and hotel facilities
        '''
        permission_classes = [permissions.IsAuthenticated]
        serializer = HotelSerializer(data=request.data)
        room_serializer = HotelRoomSerializer(data=request.data['hotel_rooms'])

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
