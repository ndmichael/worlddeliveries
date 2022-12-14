# Generated by Django 4.1.1 on 2022-09-23 09:07

import datetime
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0009_alter_itemdetail_date_shipped_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdetail',
            name='date_shipped',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 9, 7, 35, 335475, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='itemdetail',
            name='delivery_frame',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 9, 7, 35, 335475, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='itemreciever',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='itemsender',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
