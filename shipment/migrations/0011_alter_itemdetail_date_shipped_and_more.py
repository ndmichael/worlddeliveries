# Generated by Django 4.1.1 on 2022-09-26 06:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0010_alter_itemdetail_date_shipped_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdetail',
            name='date_shipped',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 27, 6, 2, 37, 118876, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='itemdetail',
            name='delivery_frame',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 3, 6, 2, 37, 118876, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='itemdetail',
            name='image',
            field=models.ImageField(default='avatar.png', upload_to='package_photos'),
        ),
    ]