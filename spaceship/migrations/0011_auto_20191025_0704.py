# Generated by Django 2.2.6 on 2019-10-25 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spaceship', '0010_auto_20191024_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyerwithseller',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]