# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BuyInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    size = models.TextField(blank=True, null=True)
    ori_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    exchange = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    buy_fees = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    final_rmb = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    buyer = models.TextField(blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    operatortime = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BUY_INFO'


class PubBuyer(models.Model):
    username = models.TextField(blank=True, null=True)
    buyer = models.TextField(blank=True, null=True)
    nickename = models.TextField(blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    operatortime = models.DateTimeField(blank=True, null=True)
    prcentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PUB_BUYER'


class PubGoods(models.Model):
    category = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    sku = models.TextField(blank=True, null=True)
    is_open = models.IntegerField(blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    operatortime = models.DateTimeField(blank=True, null=True)
    styles = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PUB_GOODS'


class PubSeller(models.Model):
    username = models.TextField(blank=True, null=True)
    seller = models.TextField(blank=True, null=True)
    nickname = models.TextField(blank=True, null=True)
    prcentage = models.FloatField(blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    operatortime = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PUB_SELLER'


class PubShoeBrand(models.Model):
    brand = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PUB_SHOE_BRAND'


class PubSnkrsSize(models.Model):
    brand = models.CharField(max_length=10, blank=True, null=True)
    us_size = models.FloatField(blank=True, null=True)
    cn_size = models.FloatField(blank=True, null=True)
    style = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PUB_SNKRS_SIZE'


class PubSnkrsStyle(models.Model):
    style_num = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    style_name = models.TextField(blank=True, null=True)
    style = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    operator = models.TextField(db_column='Operator', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PUB_SNKRS_STYLE'


class PubStoreInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.TextField(blank=True, null=True)
    store = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PUB_STORE_INFO'


class SellInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    platform = models.TextField(blank=True, null=True)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sell_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    express_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    seller = models.TextField(blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    operatortime = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    sell_times = models.IntegerField(blank=True, null=True)
    sell_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SELL_INFO'


class ShipCnInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    ship_num = models.TextField(blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)
    ship_store = models.TextField(blank=True, null=True)
    ship_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SHIP_CN_INFO'


class ShipInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    express = models.CharField(max_length=10, blank=True, null=True)
    ship_num = models.CharField(max_length=20, blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)
    ship_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SHIP_INFO'


class ShipInternaInfo(models.Model):
    id = models.ForeignKey('Warehouse', models.DO_NOTHING, db_column='id', primary_key=True)
    ship_number = models.CharField(max_length=50, blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)
    ship_store = models.TextField(blank=True, null=True)
    ship_status = models.TextField(blank=True, null=True)
    ship_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ship_unit = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SHIP_INTERNA_INFO'


class ShipSellShip(models.Model):
    number = models.CharField(max_length=20, blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SHIP_SELL_SHIP'


class SnkrsInstoreInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    style_num = models.CharField(max_length=20, blank=True, null=True)
    size = models.FloatField()
    ori_price = models.FloatField()
    exchange_rate = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)
    final_price = models.FloatField(blank=True, null=True)
    rmb = models.FloatField()
    buyer = models.CharField(max_length=10, blank=True, null=True)
    buy_date = models.DateField(blank=True, null=True)
    operator = models.TextField(db_column='Operator', blank=True, null=True)  # Field name made lowercase.
    store_location = models.CharField(max_length=10, blank=True, null=True)
    purchase_method = models.CharField(max_length=10, blank=True, null=True)
    card = models.CharField(max_length=10, blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SNKRS_INSTORE_INFO'


class SnkrsOnlineInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    style_num = models.CharField(max_length=20, blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    ori_price = models.FloatField(blank=True, null=True)
    exchange_rate = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)
    final_price = models.FloatField(blank=True, null=True)
    rmb = models.FloatField(blank=True, null=True)
    buyer = models.CharField(max_length=10, blank=True, null=True)
    buy_date = models.DateField(blank=True, null=True)
    website = models.CharField(max_length=10, blank=True, null=True)
    order_num = models.CharField(max_length=20, blank=True, null=True)
    destination = models.CharField(max_length=10, blank=True, null=True)
    ship_status = models.CharField(max_length=10, blank=True, null=True)
    card = models.CharField(max_length=10, blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SNKRS_ONLINE_INFO'


class SnkrsSale(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    platform = models.CharField(max_length=10, blank=True, null=True)
    sale_price = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)
    final_price = models.FloatField(blank=True, null=True)
    saler_ratio = models.FloatField(blank=True, null=True)
    sale_date = models.DateField(blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)
    sale_photo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SNKRS_SALE'


class Warehouse(models.Model):
    id = models.ForeignKey(ShipInternaInfo, models.DO_NOTHING, db_column='id', primary_key=True)
    goods = models.ForeignKey(PubGoods, models.DO_NOTHING, blank=True, null=True)
    buyer = models.ForeignKey(PubBuyer, models.DO_NOTHING, blank=True, null=True)
    seller = models.ForeignKey(PubSeller, models.DO_NOTHING, blank=True, null=True)
    store = models.ForeignKey(PubStoreInfo, models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WAREHOUSE'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
