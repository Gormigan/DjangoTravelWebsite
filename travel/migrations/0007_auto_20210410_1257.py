# Generated by Django 3.1.1 on 2021-04-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0006_auto_20210410_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='number_places_adults',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='number_places_children',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='price_adult',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='price_child',
            field=models.IntegerField(null=True),
        ),
    ]
