# Generated by Django 2.2.6 on 2019-10-24 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spaceship', '0009_auto_20191024_0312'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipCnInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.CharField(max_length=20, verbose_name='Ids')),
                ('ship_number', models.CharField(blank=True, max_length=50, verbose_name='ShipNumber')),
                ('ship_store', models.CharField(blank=True, max_length=50, verbose_name='ShipStore')),
                ('ship_status', models.CharField(blank=True, max_length=50, verbose_name='ShipStore')),
                ('creat_date', models.DateTimeField(auto_now=True, verbose_name='CreatDate')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='UpdateDate')),
                ('operator', models.CharField(blank=True, max_length=50, verbose_name='Operator')),
                ('operatortime', models.DateTimeField(auto_now=True, verbose_name='OperatorTime')),
                ('remark', models.CharField(blank=True, max_length=128, verbose_name='Remark')),
            ],
        ),
        migrations.CreateModel(
            name='StoreInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=20, verbose_name='Country')),
                ('store', models.CharField(blank=True, max_length=128, verbose_name='Store')),
                ('operator', models.CharField(blank=True, max_length=50, verbose_name='Operator')),
                ('operatortime', models.DateTimeField(auto_now=True, verbose_name='OperatorTime')),
                ('remark', models.CharField(blank=True, max_length=128, verbose_name='Remark')),
            ],
        ),
        migrations.RemoveField(
            model_name='shipinterinfo',
            name='cn_number',
        ),
        migrations.RemoveField(
            model_name='shipinterinfo',
            name='cn_store',
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.CharField(max_length=20, verbose_name='Ids')),
                ('status', models.CharField(blank=True, max_length=30, verbose_name='Status')),
                ('buy_info', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='spaceship.BuyInfo')),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='warehouse_buyer', to='spaceship.BuyerWithSeller')),
                ('goods', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spaceship.GoodsInfo')),
                ('sell_info', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='spaceship.SellInfo')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='warehouse_seller', to='spaceship.BuyerWithSeller')),
                ('ship_cn_info', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='spaceship.ShipCnInfo')),
                ('ship_inter_info', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='spaceship.ShipInterInfo')),
            ],
        ),
    ]