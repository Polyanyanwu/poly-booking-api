# Generated by Django 4.1.1 on 2022-11-15 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_hotelroomfacility_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='generalfacility',
            unique_together={('hotel_id', 'facility')},
        ),
    ]
