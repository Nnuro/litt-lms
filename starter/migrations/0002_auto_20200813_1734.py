# Generated by Django 3.0.6 on 2020-08-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='CompanyName',
            field=models.CharField(blank=True, max_length=100, verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=100, verbose_name='Location'),
        ),
    ]
