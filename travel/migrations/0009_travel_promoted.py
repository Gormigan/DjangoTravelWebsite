# Generated by Django 3.1.1 on 2021-04-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0008_travel_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='promoted',
            field=models.BooleanField(default=False),
        ),
    ]
