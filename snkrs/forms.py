from django import forms
from django.forms import modelformset_factory
from .models import *
from .config import *
import datetime

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='密码',widget=forms.PasswordInput(attrs={'class':'form-control'}))


class newSKUform(forms.Form):
    style_num = forms.CharField(max_length=20,
                                error_messages={'max_length':'最多20字符'},
                                label="SKU码（必填）最多20字符",
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'palceholder':'XXXXXX-XXX'}))
    style_name = forms.CharField(max_length=30,
                                 error_messages={'max_length':'最多20字符'},
                                 label="船名（必填）",
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    brand = forms.ChoiceField(choices=PubShoeBrand.objects.all().values_list('brand','brand'),
                              widget=forms.Select(attrs={'class':'select2 form-control',
                                                         'id':'brand_select',
                                                         'style':'width: 100%;'}),label="品牌")
    style = forms.ChoiceField(choices=((b,b) for b in SHOE_STYLE),
                              widget=forms.Select(attrs={'class':'form-control select2',
                                                         'id':'style_select',
                                                         'style':'width: 100%;'}),
                              label="款式")
    remark = forms.CharField(label='备注',
                             max_length=50,
                             required=False,
                             widget=forms.Textarea(attrs={'class':'form-control',
                                                          'rows':'2'}))


class newBought(forms.Form):
    buy_date = forms.CharField(label="购买日期",
                               initial=datetime.date.today(),
                               widget=forms.TextInput(attrs={"id":"datepicker",
                                                             "class":"datepicker form-control"}))
    style_num = forms.CharField(max_length=20,
                                error_messages={'max_length':'最多20字符'},
                                label= "SKU码（必填）最多20字符",
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'palceholder':'XXXXXX-XXX'}))
    size = forms.CharField(label= "鞋码（多双用','隔开）",
                           widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'rows':'3'}))
    store_location = forms.CharField(label="购买店铺",
                                     widget=forms.TextInput(attrs={"class":"form-control"}))
    ori_price = forms.CharField(label="价格（外币）",
                                widget=forms.TextInput(attrs={"class":"form-control"}))
    taxs = forms.CharField(label="消费税",
                           initial="0.0825",
                           widget=forms.TextInput(attrs={"class":"form-control"}))

    exchange_rate = forms.CharField(label="汇率",
                                    initial="7.09",
                                    widget=forms.TextInput(attrs={"class":"form-control"}))
    fees = forms.FloatField(label="小费（外币）",
                           initial="0",
                           widget=forms.TextInput(attrs={"class":"form-control"}))

    brand = forms.ChoiceField(choices=PubShoeBrand.objects.all().values_list('brand','brand'),
                              widget=forms.Select(attrs={'class':'form-control select2',
                                                         'style':'width: 100%;'}),label="品牌")
    remark = forms.CharField(label='备注',
                             max_length=50,
                             required=False,
                             widget=forms.Textarea(attrs={'class':'form-control',
                                                         'rows':'2'}))


class Goods(forms.ModelForm):
    # modelformset_factory(model=PubGoods,forms=)
    pass
class ModelFormSet(object):
    def __init__(self,username,status):
        self.username =username
        self.valude_user(username,status)

    def valude_user(self,username,status):
        num = PubUser.objects.filter(username=username,usr_status=status).count()
        print("num",num)
        if num == 0:
            new_user={}
            new_user['username'] = username
            new_user['buyer'] = username
            new_user['nickname'] = username
            new_user['operator'] = username
            new_user['operatortime'] = str(datetime.datetime.now())
            new_user['prcentage'] = '1.00'
            new_user['usr_status'] = status
            PubUser.objects.create(**new_user)


    def get_form_from_pubuser(self):
        return modelformset_factory(PubUser,fields=(['nickname']),
                                    widgets={
                                        'nickname':forms.ChoiceField(
                                            choices=PubUser.objects.filter(username=self.username).values_list('id','nickname'),
                                            widget=forms.Select(attrs={
                                                'class':'form-control select2'}),
                                            label="采购者")})

    def get_warehouse_in_form(self):
        return modelformset_factory(model=Warehouse, form=newSKUform)
        pass
#    fields=(['status','goods.category']),
# widgets={
#     'status':forms.ChoiceField(
#         choices=tuple(GOODS_STATUS.items()),
#         label="货物阶段状态",
#         widget=forms.Select(attrs={
#             'class':'form-control'
#         })
#     ),
#     'goods.category':forms.CharField(
#         label="商品目录",
#         widget=forms.TextInput(attrs={
#             'class':'form-control'
#         })
#     )
# })