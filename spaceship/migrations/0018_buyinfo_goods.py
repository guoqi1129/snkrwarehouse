# Generated by Django 2.2.6 on 2019-10-28 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spaceship', '0017_remove_news_dst_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyinfo',
            name='goods',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spaceship.GoodsInfo'),
            preserve_default=False,
        ),
    ]
