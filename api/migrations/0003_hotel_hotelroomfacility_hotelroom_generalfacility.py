# Generated by Django 4.1.1 on 2022-09-27 11:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_alter_facilitycode_name_alter_roomtype_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brief_description', models.CharField(max_length=256)),
                ('full_description', models.TextField()),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('address', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=200)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_name', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('free_cancel_limit', models.SmallIntegerField(blank=True, null=True)),
                ('prepayment_needed', models.BooleanField(blank=True, default=False, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HotelRoomFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hotel_facility', to='api.facilitycode')),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_id', to='api.hotel')),
                ('room_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hotel_room_type', to='api.roomtype')),
            ],
        ),
        migrations.CreateModel(
            name='HotelRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('on_sale', models.BooleanField(default=False)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('breakfast_included', models.BooleanField(default=False)),
                ('quantity', models.SmallIntegerField(default=0)),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel', to='api.hotel')),
                ('room_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='room_type', to='api.roomtype')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='general_facility', to='api.facilitycode')),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facility_hotel_id', to='api.hotel')),
            ],
        ),
    ]
