from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    org = models.CharField('Organization',max_length=128,blank=True)
    names = models.CharField('Names',max_length=10,blank=True)
    country = models.CharField('Country',max_length=20,blank=True)
    telephone = models.CharField('Telephone',max_length=50,blank=True)
    email = models.CharField('Email',max_length=50,blank=True)
    user_status = models.CharField('UserStatus', max_length=20,blank=True)
    user_groups = models.CharField('UserGroups', max_length=20,blank=True)
    modify_date = models.DateTimeField('LastModified', auto_now=True)
    login_time = models.DateTimeField('LastLogin', auto_now=True)
    invite_code = models.CharField('InviteCode', max_length=20, blank=True)
    invite_people = models.CharField('InvitePeople', max_length=50, blank=True)
    alipay = models.CharField('alipay', max_length=50, blank=True)
    special_sign1 = models.CharField('special_sign1', max_length=50, blank=True)  #个性签名
    special_sign2 = models.CharField('special_sign2', max_length=10, blank=True)  #状态显示

    class Meta:
        verbose_name = 'User Profile'


class BuyerWithSeller(models.Model):
    username = models.CharField('Username',max_length=50,blank=True)
    buyer = models.CharField('Buyer',max_length=50,blank=True)
    nickname = models.CharField('NickName',max_length=50,blank=True)
    status = models.CharField('Status',max_length=50,blank=True)
    substatus = models.CharField('SubStatus',max_length=50,blank=True)
    operator = models.CharField('Operator',max_length=50,blank=True)
    operatortime = models.DateTimeField('OperatorTime',auto_now=True)
    percentage = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Buyer and Seller'


class StoreInfo(models.Model):
    country = models.CharField('Country',max_length=20,blank=True)
    store = models.CharField('Store',max_length=128,blank=True)
    operator = models.CharField('Operator',max_length=50,blank=True)
    operatortime = models.DateTimeField('OperatorTime',auto_now=True)
    remark = models.CharField('Remark',max_length=128,blank=True)

    def __str__(self):
        return self.store


class GoodsInfo(models.Model):
    buy_date = models.DateTimeField('BuyDate',auto_now=True)
    category = models.CharField('Category',max_length=30,blank=True)
    brand = models.CharField('Brand',max_length=30,blank=True)
    styles = models.CharField('Styles',max_length=1,blank=True)
    name = models.CharField('Name',max_length=128,blank=True)
    sku = models.CharField('Sku',max_length=50,blank=True)
    store = models.ForeignKey(StoreInfo,on_delete=models.CASCADE)
    isopen = models.CharField('IsOpen',max_length=1,blank=True)
    operator = models.CharField('Operator',max_length=50,blank=True)
    operatortime = models.DateTimeField('OperatorTime',auto_now=True)
    remark = models.CharField('Operator',max_length=128,blank=True)

    def __str__(self):
        return self.sku

    class Meta:
        verbose_name = 'Goods Info'


class BuyInfo(models.Model):
    ids = models.CharField("Ids",max_length=20)
    goods = models.ForeignKey(GoodsInfo,on_delete=models.CASCADE)
    size = models.CharField('Size',max_length=5,blank=True)
    ori_price = models.DecimalField(max_digits=10,decimal_places=2)
    exchange = models.DecimalField(max_digits=10,decimal_places=2)
    buy_fees = models.DecimalField(max_digits=10,decimal_places=2)
    tax = models.DecimalField(max_digits=10,decimal_places=2)
    final_price = models.DecimalField(max_digits=10,decimal_places=2)
    final_rmb = models.DecimalField(max_digits=10,decimal_places=2)
    buyer = models.ForeignKey(BuyerWithSeller,on_delete=models.SET_NULL,null=True)
    remark = models.CharField('Remark',max_length=128,blank=True)
    operator = models.CharField('Operator',max_length=50,blank=True)
    operatortime = models.DateTimeField('OperatorTime',auto_now=True)

    def __str__(self):
        return str(self.final_rmb)


class SellInfo(models.Model):
    ids = models.CharField("Ids",max_length=20)
    platform = models.CharField('PlatForm', max_length=10,blank=True)
    sell_rmb = models.DecimalField(max_digits=10,decimal_places=2)
    sell_fee = models.DecimalField(max_digits=10,decimal_places=2)
    express_fee = models.DecimalField(max_digits=10,decimal_places=2)
    final_rmb = models.DecimalField(max_digits=10,decimal_places=2)
    seller = models.CharField('Seller', max_length=10,blank=True)
    sell_times = models.DecimalField(max_digits=10,decimal_places=0)
    sell_date = models.DateTimeField('SellDate',auto_now=True)
    operator = models.CharField('Operator',max_length=50,blank=True)
    operatortime = models.DateTimeField('OperatorTime',auto_now=True)
    remark = models.CharField('Remark',max_length=128,blank=True)

    def __str__(self):
        return self.final_rmb


class ShipInterInfo(models.Model):
    ids = models.CharField("Ids",max_length=20)
    ship_number = models.CharField('ShipNumber',max_length=50,blank=True)
    ship_store = models.CharField('ShipStore',max_length=50,blank=True)
    ship_status = models.CharField('ShipStatus',max_length=50,blank=True)
    ship_unit = models.CharField('ShipUnit',max_length=50,blank=True)
    ship_fee = models.DecimalField(max_digits=10,decimal_places=2)
    exchange_fee = models.DecimalField(max_digits=10,decimal_places=2)
    ship_rmb = models.DecimalField(max_digits=10,decimal_places=2)
    creat_date = models.DateTimeField('CreatDate',auto_now=True)
    update_date = models.DateTimeField('UpdateDate',auto_now=True)
    operator = models.CharField('Operator',max_length=50,blank=True)
    operatortime = models.DateTimeField('OperatorTime',auto_now=True)
    remark = models.CharField('Remark',max_length=128,blank=True)
    def __str__(self):
        return self.ship_rmb


class ShipCnInfo(models.Model):
    ids = models.CharField("Ids",max_length=20)
    ship_number = models.CharField('ShipNumber',max_length=50,blank=True)
    ship_store = models.CharField('ShipStore',max_length=50,blank=True)
    ship_status = models.CharField('ShipStore',max_length=50,blank=True)
    creat_date = models.DateTimeField('CreatDate',auto_now=True)
    update_date = models.DateTimeField('UpdateDate',auto_now=True)
    operator = models.CharField('Operator',max_length=50,blank=True)
    operatortime = models.DateTimeField('OperatorTime',auto_now=True)
    remark = models.CharField('Remark',max_length=128,blank=True)

    def __str__(self):
        return self.ship_number


class Warehouse(models.Model):
    ids = models.CharField("Ids",max_length=20)
    goods = models.ForeignKey(GoodsInfo,blank=True,on_delete=models.SET_NULL,null=True)
    buyer = models.ForeignKey(BuyerWithSeller,blank=True,related_name='warehouse_buyer',on_delete=models.SET_NULL,null=True)
    seller = models.ForeignKey(BuyerWithSeller,blank=True,related_name='warehouse_seller',on_delete=models.SET_NULL,null=True)
    buy_info = models.OneToOneField(BuyInfo,blank=True,on_delete=models.CASCADE)
    sell_info = models.OneToOneField(SellInfo,blank=True,on_delete=models.CASCADE)
    ship_inter_info = models.OneToOneField(ShipInterInfo,blank=True,on_delete=models.CASCADE)
    ship_cn_info = models.OneToOneField(ShipCnInfo,blank=True,on_delete=models.CASCADE)
    status = models.CharField('Status',max_length=30,blank=True)
    time1 = models.DateField('Time1',auto_now=True)
    time2 = models.DateField('Time2',auto_now=True)
    time3 = models.DateField('Time3',auto_now=True)
    time4 = models.DateField('Time4',auto_now=True)
    time5 = models.DateField('Time5',auto_now=True)
    time6 = models.DateField('Time6',auto_now=True)
    time7 = models.DateField('Time7',auto_now=True)


class News(models.Model):
    news = models.CharField('News',max_length=128,blank=True)
    creat_time = models.DateTimeField('CreatTime',auto_now=True)
    status = models.CharField('Status',max_length=30,blank=True)
    style = models.CharField('Style',max_length=30,blank=True)
    remark = models.CharField('Remark',max_length=128,blank=True)
    creat_user = models.ForeignKey(User,blank=True,on_delete=models.SET_NULL, null=True,related_name="creatUser")
    operate_time = models.DateTimeField('OperateTime',auto_now=True)

class UserAndNews(models.Model):
    users = models.ForeignKey(User,blank=True,on_delete=models.SET_NULL, null=True)
    news = models.ForeignKey(News,blank=True,on_delete=models.SET_NULL, null=True)

class BuyerMatchSeller(models.Model):
    buyer=models.ForeignKey(BuyerWithSeller,on_delete=models.CASCADE,related_name='abuyer')
    seller=models.ForeignKey(BuyerWithSeller,on_delete=models.CASCADE,related_name='aseller')




