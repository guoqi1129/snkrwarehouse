# Generated by Django 2.2.6 on 2019-10-26 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceship', '0011_auto_20191025_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyerwithseller',
            name='substatus',
            field=models.CharField(blank=True, max_length=50, verbose_name='SubStatus'),
        ),
    ]
