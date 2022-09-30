from rest_framework import serializers

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


class HotelRoomSerializer(serializers.ModelSerializer):
    # hotel_id = HotelSerializer(many=True, read_only=True)

    class Meta:
        model = HotelRoom
        fields = ('id', 'hotel_id', 'room_type',
                  'price', 'on_sale', 'quantity', 'sale_price',
                  'breakfast_included')


class HotelSerializer(serializers.ModelSerializer):

    # hotel_rooms = serializers.StringRelatedField(many=True)
    hotel_rooms = HotelRoomSerializer(many=True, read_only=True)
    hotel_general_facility = GeneralFacilitySerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'brief_description',
                  'full_description', 'rating', 'address', 'city',
                  'contact_email', 'contact_name', 'contact_phone',
                  'image_url', 'image', 'free_cancel_limit',
                  'prepayment_needed', 'hotel_rooms', 'hotel_general_facility']
