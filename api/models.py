from django.db import models

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
