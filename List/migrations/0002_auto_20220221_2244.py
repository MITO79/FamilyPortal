# Generated by Django 3.2.9 on 2022-02-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ta_list',
            name='sub_1',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='ta_list',
            name='sub_10',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='ta_list',
            name='sub_2',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='ta_list',
            name='sub_3',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='ta_list',
            name='sub_4',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='ta_list',
            name='sub_5',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='ta_list',
            name='sub_6',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='ta_list',
            name='sub_7',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='ta_list',
            name='sub_8',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='ta_list',
            name='sub_9',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='ta_list',
            name='content',
            field=models.CharField(default='', max_length=255),
        ),
    ]