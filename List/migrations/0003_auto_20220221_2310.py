# Generated by Django 3.2.9 on 2022-02-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0002_auto_20220221_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='ta_list',
            name='date_1',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='ta_list',
            name='date_2',
            field=models.DateTimeField(null=True),
        ),
    ]