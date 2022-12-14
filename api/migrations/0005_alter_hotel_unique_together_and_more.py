# Generated by Django 4.1.1 on 2022-10-01 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_generalfacility_hotel_id_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hotel',
            unique_together={('name', 'city')},
        ),
        migrations.AlterUniqueTogether(
            name='hotelroom',
            unique_together={('hotel_id', 'room_type')},
        ),
    ]
