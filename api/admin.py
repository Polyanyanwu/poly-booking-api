""" Admin config and for hotel tables """
from django.contrib import admin

from django.contrib import admin
from .models import Hotel, GeneralFacility, HotelRoom, HotelRoomFacility


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brief_description',
                    'full_description', 'rating', 'address', 'city',
                    'contact_email', 'contact_name', 'contact_phone',
                    'image_url', 'image', 'free_cancel_limit',
                    'prepayment_needed', 'created_by'
                    )


@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel_id', 'room_type',
                    'price', 'on_sale', 'quantity', 'sale_price',
                    'breakfast_included')


@admin.register(HotelRoomFacility)
class HotelRoomFacilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel_id', 'room_type',
                    'facility')


@admin.register(GeneralFacility)
class GeneralFacilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel_id', 'facility')
