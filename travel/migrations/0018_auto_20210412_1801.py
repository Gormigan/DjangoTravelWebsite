# Generated by Django 3.1.1 on 2021-04-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0017_auto_20210412_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='image',
            field=models.ImageField(null=True, upload_to='travel/'),
        ),
    ]
