# Generated by Django 2.2.5 on 2019-09-11 03:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190910_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 11, 3, 11, 53, 457357, tzinfo=utc)),
        ),
    ]
