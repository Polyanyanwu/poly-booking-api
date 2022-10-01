
import math
from django import template
from api.models import RoomType
from django.utils.numberformat import Decimal

register = template.Library()


@register.filter(name='api_codes')
def code_name(table, code):
    if table == 'room_type':
        record = RoomType.objects.filter(pk=code)
        if record:
            return record[0].name
        return ""


@register.filter(name='rating_string')
def get_rating_string(rating):
    print("type rating==", type(rating))
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
