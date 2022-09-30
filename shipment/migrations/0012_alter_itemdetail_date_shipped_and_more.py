# Generated by Django 4.1.1 on 2022-09-30 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0011_alter_itemdetail_date_shipped_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdetail',
            name='date_shipped',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 1, 18, 51, 37, 74920, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='itemdetail',
            name='delivery_frame',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 7, 18, 51, 37, 75920, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='problem_type',
            field=models.CharField(choices=[('none', 'No Problems'), ('paperwork', 'PAPERWORK_OVERLOAD'), ('custom clerance', 'CUSTOM CLEARANCE'), ('bad weather', 'BAD WEATHER')], default='no problem', max_length=100),
        ),
    ]