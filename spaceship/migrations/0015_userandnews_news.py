# Generated by Django 2.2.6 on 2019-10-26 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spaceship', '0014_news_userandnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='userandnews',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spaceship.News'),
        ),
    ]
