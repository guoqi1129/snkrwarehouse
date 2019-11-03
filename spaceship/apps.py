from django.apps import AppConfig
from.configs import *
from . import models
from . import forms
from .models import BuyerWithSeller
from django.contrib.auth.models import User as UserObject
from . import configs
from django.forms.models import model_to_dict
from django.core import serializers
import datetime


class SpaceshipConfig(AppConfig):
    name = 'spaceship'


class User(object):
    def __init__(self, user):
        self.username = user
        self.profile = None
        self.item = None
        self.profile = None
        self.user_profile = None
        self.tem = None
        self.team = SellerTeam(self)
        self.user = UserObject.objects.get(username=self.username)
        self.information = userInformation(self.username)
        self.update_content()

    def update_content(self):
        self.profile = models.UserProfile.objects.get(user__username__exact=self.username)
        self._get_item()
        self.information.update_news()
        self.user_profile = model_to_dict(self.profile)
        self.get_tem()

    def new_status(self, status, status_detail):
        self.information.set_status(status, status_detail)

    def _get_item(self):
        items = configs.ITEMS_USER[self.profile.user_groups]
        self.item = {}
        for i,j in configs.ITEMS_DETAIL.items(): #i是父目录
            son_item = []
            for m,n in list(j.values())[0].items():      #m,n in {'11': '库存新增', '12': '买到鞋了', '13': '卖出鞋啦'}
                if m in items:
                    son_item.append({n:ITEM_URLS.get(m)})
            if len(son_item)>0:
                self.item[i]= {list(j.keys())[0]:son_item}

    def get_tem(self):
        tem = self._get_message()
        tem.update(self._get_module_items())
        # tem.update(self._prepare_form_message())
        self.tem = tem

    def set_inform(self, info):
        self.tem['inform'] = info

    def _get_message(self):
        self.information.update_news()
        return {'message':self.information}

    def _get_module_items(self):
        return {'item':self.item}

    def _prepare_form_message(self):
        return None

    def warehouse_in_search(self, keywords):
        q1 = models.GoodsInfo.objects.filter(name__icontains=keywords)
        q2 = models.GoodsInfo.objects.filter(sku__icontains=keywords)
        q3 = q1 | q2
        data = q3.values('category','brand','name','sku','styles')
        return data

    def warehouse_in_save(self,request):
        buy_date = request.POST.get('buy_date')
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        styles = request.POST.get('style')
        name = request.POST.get('name')
        sku = request.POST.get('sku')
        remark = request.POST.get('remark')
        country = request.POST.get('country')
        store = request.POST.get('store')
        ori_price = request.POST.get('ori_price')
        exchange = request.POST.get('exchange')
        tax = request.POST.get('taxes')
        fees = request.POST.get('fees')
        buyer = request.POST.get('nickname')
        operator = request.user.username
        sizes = request.POST.get('size')
        sizes = sizes.split(',')
        a = []
        try:
            final_price = float(ori_price)*(1+float(tax)/100)+float(fees)
            final_rmb = final_price*float(exchange)
            final_price = str(final_price)
            final_rmb = str(final_rmb)
        except:
            return {'error':'价格相关内容填写错误'}
        for size in sizes:
            if "*" in size:
                b = size.split("*")
                for i in range(int(b[1])):
                    a.append(b[0])
            else:
                a.append(size)

        try:
            store = models.StoreInfo.objects.get(country__exact= country,
                                                store__exact=store,
                                                operator__exact=operator)
        except:
            store_info = {'country': country, 'store': store,
                          'operator':operator}
            store = models.StoreInfo.objects.create(**store_info)
        try:
            goods = models.GoodsInfo.objects.get(category__exact=category,
                                                      brand__iexact= brand,
                                                      styles__iexact=styles,
                                                      name__iexact=name,
                                                      sku__iexact=sku,
                                                      operator__iexact= operator)
        except:
            goods_info = {'category': category, 'brand': brand, 'styles': styles,
                          'name': name, 'sku': sku, 'operator': operator,
                          'remark': remark,'buy_date':buy_date,'store':store}
            goods = models.GoodsInfo.objects.create(**goods_info)
        for size in a:
            buy_info = {'size':size, 'ori_price':ori_price, 'exchange':exchange,
                        'buy_fees':fees, "tax":tax, 'final_price':final_price,
                        'final_rmb': final_rmb, 'buyer_id':buyer, 'operator':operator,
                        'goods':goods}
            buy = models.BuyInfo.objects.create(**buy_info)
            sell_info = {
                'sell_rmb':0,
                'sell_fee':0,
                'express_fee':0,
                'final_rmb':0,
                'sell_times':0}
            sell = models.SellInfo.objects.create(**sell_info)
            ship_inter_info = {'ship_fee':0,
                               'exchange_fee':0,
                               'ship_rmb':0}
            ship_inter = models.ShipInterInfo.objects.create(**ship_inter_info)
            ship_cn_info = {}
            ship_cn = models.ShipCnInfo.objects.create(**ship_cn_info)
            warehouse = {'status': configs.WAREHOUSE_STATUS['1'],
                         'buy_info': buy,
                         'goods': goods,
                         'sell_info': sell,
                         'ship_inter_info': ship_inter,
                         'ship_cn_info': ship_cn,
                         'ids':'0',
                         'time1': datetime.datetime.now().strftime('%Y-%m-%d')
                         }
            warehouse = models.Warehouse.objects.create(**warehouse)
        return None

    def get_my_shoe_table(self,a):
        if a=='1':
            q1 = models.BuyInfo.objects.filter(buyer__username__exact=self.username,
                                               buyer__status__exact='1',
                                               warehouse__status__in=list(configs.WAREHOUSE_STATUS.values())[0:2],
                                               )

            data = q1.values('id','final_price','final_rmb','size','goods__category','goods__brand',
                             'goods__styles','goods__name','goods__sku','warehouse__status',
                             'operatortime')
            return data
        elif a=='2':
            q1 =models.Warehouse.objects.filter(buy_info__buyer__username__exact=self.username,
                                                buy_info__buyer__status__exact='1',
                                                status__in=list(configs.WAREHOUSE_STATUS.values())[1:6],
                                                ids='0')
            data = q1.values('id','status','goods__category','goods__brand','goods__styles','goods__name',
                             'buy_info__operatortime','goods__sku','buy_info__final_rmb','buy_info__size',
                             'ship_inter_info__ship_store','ship_inter_info__ship_number','goods__remark',
                             'ship_inter_info__ship_rmb','ship_inter_info__creat_date','time2','time3','time4','time5')
            return data
        elif a=="3":
            q1 = models.Warehouse.objects.filter(seller__nickname__iexact=self.username,
                                                 seller__status__exact='1',
                                                 status__in=list(configs.WAREHOUSE_STATUS.values())[5:7])
            data = q1.values('id','status','goods__category','goods__brand','goods__styles','goods__name',
                             'goods__sku','buy_info__final_rmb','buy_info__size','goods__remark','time2','time3','time4','time5')
            return data

    def get_my_shoe_child_table(self,data):
        start = datetime.datetime.now() - datetime.timedelta(days=30,hours=0, minutes=0, seconds=0)
        q2 = models.BuyInfo.objects.filter(buyer__username__exact=self.username,
                                           buyer__status__exact='1',
                                           operatortime__gte=start,
                                           goods_id=data.get('id'))
        return q2.values('id','size','ori_price','exchange','buy_fees','tax','final_price','final_rmb','operatortime','warehouse__status')

    def warehouse_in_return(self,data=None):
        title = {"title":"仓库新增"}
        form_goods = forms.GoodsInfoForm(self,data)
        form_buyinfo = forms.BuyInfoForm(self.username,data)
        form_storeinfo = forms.StoreInfoForm(self,data)
        tem = self.tem
        tem.update({'form_goods':form_goods,
                    'form_buyinfo':form_buyinfo,
                    'form_storeinfo':form_storeinfo})
        tem.update(title)
        return tem

    def ship_my_shoes(self,POST):
        id = POST.get('id')
        ship_store = POST.get('ship_store')
        ship_number = POST.get('ship_number')
        ship_rmb = POST.get('ship_rmb')
        seller = POST.get('seller')
        data = {'ship_store':ship_store,'ship_number':ship_number,'ship_rmb':ship_rmb,
                'ship_fee':0,'exchange_fee':0}
        print('seller',seller)
        ship_inter_info = models.ShipInterInfo.objects.create(**data)
        models.Warehouse.objects.filter(buy_info_id__exact=id).update(ship_inter_info=ship_inter_info,
                                                                        status=configs.WAREHOUSE_STATUS['2'],
                                                                      seller_id=seller,
                                                                      time2=datetime.datetime.now().strftime('%Y-%m-%d'))

        return {'inform': '发货成功'}

    def update_status(self,key,id):
        warehouse = models.Warehouse.objects.filter(id=id)
        if key=="ship_to_china":
            if list(warehouse.values_list('status'))[0][0] == configs.WAREHOUSE_STATUS['2']:
                warehouse.update(status=configs.WAREHOUSE_STATUS['3'],
                                 time3=datetime.datetime.now().strftime('%Y-%m-%d'))

                return {'inform':'收货成功'}
            else:
                return {'inform':'状态错误，请刷新再试'}
        elif key=="ready_to_sell":
            if list(warehouse.values_list('status'))[0][0] == configs.WAREHOUSE_STATUS['3']:
                warehouse.update(status=configs.WAREHOUSE_STATUS['4'],
                                 time4=datetime.datetime.now().strftime('%Y-%m-%d'))

                return {'inform':'上架成功'}
            else:
                return {'inform':'状态错误，请刷新再试'}

        elif key=="selled":
            if list(warehouse.values_list('status'))[0][0] == configs.WAREHOUSE_STATUS['4']:
                warehouse.update(status=configs.WAREHOUSE_STATUS['5'],
                                 time5=datetime.datetime.now().strftime('%Y-%m-%d'))
                return {'inform':'售出成功'}
            else:
                return {'inform':'状态错误，请刷新再试'}

    def make_match_team_tem(self):
        tem = {'title':'匹配团队'}
        tem.update({'inform':''})
        match_team_form =forms.BuyerMatchSeller(self.username)
        tem.update({'match_team_form':match_team_form})
        tem.update(self.tem)
        return tem

    def match_team_save(self,buyer,seller):
        try:
            models.BuyerWithSeller.objects.get(id=buyer)
            models.BuyerWithSeller.objects.get(id=seller)
        except:
            return {"inform":'添加失败'}
        if models.BuyerMatchSeller.objects.filter(buyer_id=buyer,seller_id=seller).count():
            return {'inform':'添加失败，已经配对完成'}
        models.BuyerMatchSeller.objects.create(buyer_id=int(buyer),seller_id=int(seller))
        return {"inform":'添加成功'}

class FormSet(object):
    def __init__(self):
        pass


class userInformation(object):
    def __init__(self,user):
        self.username = user
        self.news = None
        self.newsNumber = None
        self.alert = None
        self.alertNumber = None
        self.status = None
        self.statusNumber = None
        self.userStatusDetail = None
        self.userStatus = None

    def update_news(self):
        self.get_news()
        self.get_alert()
        self.get_status()

    def set_status(self,status,status_detail):
        self.userStatusDetail = status_detail
        self.userStatus = status

    def get_news(self):
        self.news = [1,2]
        self.newsNumber=2
    def get_alert(self):
        self.alert = [1,2]
        self.alertNumber=2
    def get_status(self):
        self.status=[1,2]
        self.statusNumber=2
    def get_user_status(self):
        #获取用户身份
        return 0
    def send_creat_team_news(self,style,username_list,percentage_list,src_user,news,args=None):
        data = {}
        creat_user = UserObject.objects.get(username__exact=src_user)
        # news = configs.TEAM_NEWS[news].replace("src_name",src_user)
        # news = news.replace('choice',args['choice'])
        # news = news.replace('nickname',args['nickname'])
        # news = news.replace('percentage',str(percentage_list[i]))
        status = '0'        #0是未获得确认
        data = {'news':news,
                'status':status,
                'creat_user':creat_user,
                'style':style}
        news = models.News.objects.create(**data)
        for i in range(len(username_list)):     #src_name向您提出了创建choice团队nickname的申请，你的占比为percentage%
            dst_user = UserObject.objects.get(username__exact=username_list[i])
            data = {'users':dst_user,'news':news}
            models.UserAndNews.objects.create(**data)
            for online_user in list(set(username_list).intersection(set(configs.USERS.keys()))):
                configs.USERS[online_user].information.get_alert()


def get_User(username):
    if username in configs.USERS.keys():
        return configs.USERS[username]
    else:
        usr = User(username)
        configs.USERS.update({username:usr})
        return usr

class SellerTeam(object):
    def __init__(self,user):
        self.user = user
        self.username = self.user.username
        self.team = models.BuyerWithSeller.objects.filter(username=self.username).values_list("nickname")

    def save(self, POST, username_list=[], percentage_list=[],status='0'):

        data = {'buyer':POST.get('choice'),
                'username':self.username,
                'percentage':100-sum(percentage_list),
                'substatus':'1',
                'operator':self.username,
                'nickname':POST.get('nickname'),
                'status':status}
        self._save(data)
        data.update({"substatus":"0"})
        for i in range(len(percentage_list)):
            data.update({'username':username_list[i]})
            data.update({'percentage':percentage_list[i]})
            self._save(data)
            self.user.information.send_creat_team_news(style='alert',
                                           username_list=username_list,
                                           percentage_list=percentage_list,
                                           src_user=self.username,
                                           news="creat_news",
                                           args={'choice':data['buyer'],
                                                 'nickname':data['nickname']})
    def _save(self,data):
        models.BuyerWithSeller.objects.create(**data)
