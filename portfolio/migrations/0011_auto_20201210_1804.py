# Generated by Django 3.1.4 on 2020-12-10 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20201208_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_page',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 10, 18, 4, 7, 803552)),
        ),
    ]
