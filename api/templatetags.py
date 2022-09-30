
from django import template
from .models import RoomType

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
    if rating >= 4:
        return "Excellent"
    elif rating >= 3:
        return "Very Good"
    elif rating >= 2:
        return "Good"
    else:
        return "Okay"
