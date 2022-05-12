# Generated by Django 3.2.8 on 2022-05-12 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0002_alter_ta_menu_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ma_rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ta_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recipe.ta_menu')),
                ('rank', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Recipe.ma_rank')),
            ],
        ),
    ]
