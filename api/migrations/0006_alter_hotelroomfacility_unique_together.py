# Generated by Django 4.1.1 on 2022-10-01 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_hotel_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hotelroomfacility',
            unique_together={('hotel_id', 'room_type', 'facility')},
        ),
    ]
