""" Forms for API Module """

from django import forms
from .models import FacilityCode, RoomType


class FacilityCodeForm(forms.ModelForm):
    """ Facility Code form """
    class Meta:
        """ Meta for Facility Code Form """
        model = FacilityCode
        fields = '__all__'


class RoomTypeForm(forms.ModelForm):
    """ Facility Hotel Room Type form """
    class Meta:
        """ Meta for Room Type Code Form """
        model = RoomType
        fields = '__all__'
