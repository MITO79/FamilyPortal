# Generated by Django 3.2.8 on 2022-05-11 01:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ta_schedule',
            name='targetDay',
            field=models.DateField(default=datetime.date(2022, 5, 11)),
        ),
    ]
