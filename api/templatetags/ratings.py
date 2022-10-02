
import math
import requests
from datetime import timedelta, datetime
from django import template
from api.models import RoomType, FacilityCode
from django.utils.numberformat import Decimal

register = template.Library()


@register.filter(name='room_name')
def code_name(code):
    record = RoomType.objects.filter(pk=code)
    if record:
        return record[0].name
    return ""


@register.filter(name='facility_name')
def get_fac_code_name(code):
    record = FacilityCode.objects.filter(pk=int(code))
    if record:
        return record[0].name
    return ""


@register.filter(name='get_room_facilities')
def get_room_facility_codes(room_type, facilities):
    if room_type in facilities.keys():
        return facilities[int(room_type)]
    else:
        return []


@register.filter(name='date_from_now')
def get_date_from_now(hours):
    hrs = int(hours)
    today = datetime.now()
    today += timedelta(hours=hrs)
    return today


@register.filter(name='rating_string')
def get_rating_string(rating):
    rating_num = Decimal(rating)
    if rating_num >= 4:
        return "Excellent"
    elif rating_num >= 3:
        return "Very Good"
    elif rating_num >= 2:
        return "Good"
    else:
        return "Okay"


@register.filter(name='rating_main')
def get_main_rating(rating):
    """ Template tag used to return number of ratings
    """
    rating = Decimal(rating)
    return range(rating)


@register.filter(name='rating_bal')
def get_rating_balance(rating):
    """ Template tag used to return the rating minus 5
        integer rating
    """
    rating = Decimal(rating)
    return range(5-rating)


@register.filter(name='rating_dec_main')
def get_dec_main_rating(rating):
    """ Template tag used to return number of ratings
        for decimal values
    """
    rating = Decimal(rating)
    num = math.modf(rating)
    return range(int(num[1]))


@register.filter(name='rating_dec_bal')
def get_dec_bal_rating(rating):
    """ Template tag used to return number of ratings
        for decimal values
    """
    rating = Decimal(rating)
    num = math.modf(rating)
    if num[0] > 0:
        return range(4-int(num[1]))
    else:
        return range(5-int(num[1]))


@register.filter(name='rating_dec_fraction')
def get_dec_fraction_rating(rating):
    """ Template tag used to return number of ratings
        for decimal values fraction
    """
    rating = Decimal(rating)
    num = math.modf(rating)
    if num[0] > 0:
        return True
    else:
        return False
