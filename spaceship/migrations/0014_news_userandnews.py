# Generated by Django 2.2.6 on 2019-10-26 23:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spaceship', '0013_auto_20191026_0724'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAndNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.CharField(blank=True, max_length=128, verbose_name='News')),
                ('creat_time', models.DateTimeField(auto_now=True, verbose_name='CreatTime')),
                ('status', models.CharField(blank=True, max_length=30, verbose_name='Status')),
                ('remark', models.CharField(blank=True, max_length=128, verbose_name='Remark')),
                ('operate_time', models.DateTimeField(auto_now=True, verbose_name='OperateTime')),
                ('creat_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creatUser', to=settings.AUTH_USER_MODEL)),
                ('dst_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dstUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
