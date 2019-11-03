# Generated by Django 2.2.6 on 2019-11-01 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spaceship', '0021_auto_20191030_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerMatchSeller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyerwithseller', to='spaceship.BuyerWithSeller')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellerwithbuyer', to='spaceship.BuyerWithSeller')),
            ],
        ),
    ]