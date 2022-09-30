from django.db import models
from django.contrib.auth.models import User
from django.core.validators import \
    (MinLengthValidator, MinValueValidator, MaxValueValidator)
# Create your models here.


class FacilityCode(models.Model):
    """ Data model for Facility Codes """

    name = models.CharField(max_length=200, null=False,
                            blank=False, unique=True)

    def __str__(self):
        return str(self.name)


class RoomType(models.Model):
    """ Data model for Room Type Codes """

    name = models.CharField(max_length=200, null=False,
                            blank=False, unique=True)

    def __str__(self):
        return str(self.name)


class Hotel(models.Model):
    """ Model that for storing hotel summary record
        The hotel iD will be auto generated long value
    """
    name = models.CharField(max_length=200, null=False, blank=False)
    brief_description = models.CharField(max_length=256,
                                         null=False, blank=False)
    full_description = models.TextField(null=False, blank=False)
    rating = models.DecimalField(max_digits=5, decimal_places=2,
                                 validators=[MaxValueValidator(5),
                                             MinValueValidator(0)],
                                 null=True, blank=True)
    address = models.CharField(max_length=256, null=False, blank=False)
    city = models.CharField(max_length=200, null=False, blank=False)
    contact_email = models.EmailField(max_length=254, null=False, blank=False)
    contact_name = models.CharField(max_length=200, null=True, blank=True)
    contact_phone = models.CharField(max_length=50, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    free_cancel_limit = models.SmallIntegerField(null=True, blank=True)
    prepayment_needed = models.BooleanField(default=False,
                                            null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   null=True, blank=True,
                                   related_name='orders')

    def __str__(self):
        return self.name


class HotelRoom(models.Model):
    """ Model that for storing hotel room record
    """
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE,
                                 null=False, blank=False,
                                 related_name='hotel_rooms')
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL,
                                  null=True, blank=True,
                                  related_name='room_type')
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0)])
    on_sale = models.BooleanField(default=False, null=False, blank=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2,
                                     validators=[MinValueValidator(0)])
    breakfast_included = models.BooleanField(default=False)
    quantity = models.SmallIntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return self.room_type.name


class HotelRoomFacility(models.Model):
    """ Model that for storing hotel room facility records
    """
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE,
                                 null=False, blank=False,
                                 related_name='hotel_id')
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL,
                                  null=True, blank=True,
                                  related_name='hotel_room_type')
    facility = models.ForeignKey(FacilityCode, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name='hotel_facility')

    def __str__(self):
        return self.facility.name


class GeneralFacility(models.Model):
    """ Model that for storing hotel-wide facility records
    """
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE,
                                 null=False, blank=False,
                                 related_name='hotel_general_facility')
    facility = models.ForeignKey(FacilityCode, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name='general_facility')

    def __str__(self):
        return self.facility.name
