from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import \
    (FacilityCode, GeneralFacility, Hotel,
     HotelRoom, HotelRoomFacility, RoomType)


class FacilityCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityCode
        fields = ('id', 'name')


class GeneralFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralFacility
        fields = ('id', 'facility')


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ('id', 'name')


class HotelRoomFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomFacility
        fields = ('id', 'hotel_id', 'room_type', 'facility')
        # fields = '__all__'


class HotelRoomSerializer(serializers.ModelSerializer):

    # room_type = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = HotelRoom
        fields = ('id', 'hotel_id', 'room_type',
                  'price', 'on_sale', 'quantity', 'sale_price',
                  'breakfast_included')


class HotelSerializer(WritableNestedModelSerializer,
                      serializers.ModelSerializer):

    hotel_rooms = HotelRoomSerializer(many=True)
    hotel_general_facility = GeneralFacilitySerializer(many=True)

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'brief_description',
                  'full_description', 'rating', 'address', 'city',
                  'contact_email', 'contact_name', 'contact_phone',
                  'image_url', 'image', 'free_cancel_limit', 'created_by',
                  'prepayment_needed', 'hotel_rooms', 'hotel_general_facility']
