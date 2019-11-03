from django import forms
from django.contrib.auth.models import User
from . import models
import re
from . import configs
import datetime
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)
from django.forms import BaseFormSet


def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    return re.match(pattern,email)

def update_country():
     configs.COUNTRY_LIST = tuple(set(models.UserProfile.objects.values('country').values_list('country','country')))

update_country()

class RegistrationForm(forms.Form):
    username = forms.CharField(label='用户名',
                               max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control'}),
                               help_text="用户名长度6-50，密码长度6-20")
    email = forms.EmailField(label='邮箱',max_length=50,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码',max_length=20,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='密码确认',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    country = forms.ChoiceField(choices=configs.COUNTRY_LIST,
                                label='所在国家',
                                widget=forms.Select(attrs={'class': 'select2 form-control'}))
    telephone = forms.CharField(label='电话',max_length=50,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    user_groups = forms.ChoiceField(choices=configs.USER_STATIUS,
                                  label='用户身份',
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    invite_people = forms.CharField(label='邀请码',max_length=20,
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    names = forms.CharField(label='真实姓名(交易使用)',max_length=20,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    alipay = forms.CharField(label='支付宝账户(如无，可填写 银行+卡号)',max_length=50,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))


    def clean_username(self):
        username =self.cleaned_data.get('username')
        if len(username) < 6:
            raise forms.ValidationError('用户名长度小于6')
        elif len(username) > 50:
            raise forms.ValidationError('用户名长度大于50')
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError('该用户名已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email_check(email):
            filter_result = User.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                raise forms.ValidationError('邮箱已被使用')
        else:
            raise forms.ValidationError('请输入有效的邮箱地址')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError('密码太短')
        elif len(password) > 20:
            raise forms.ValidationError('密码太长')
        return password

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password!=password2:
            raise forms.ValidationError('两次输入密码不一致')
        return password2


    def clean_invite_people(self):
            invite_people = self.cleaned_data.get('invite_people').upper()
            user_groups = self.cleaned_data.get('user_groups')
            filter_result = models.UserProfile.objects.filter(invite_code__exact=invite_people)
            if len(filter_result) == 0:
                raise forms.ValidationError("无此邀请码，请重新输入")
            elif list(filter_result.values_list("user_groups"))[0][0] == 'admin' or list(filter_result.values_list("user_groups"))[0][0]  == user_groups:
                return list(filter_result.values_list("user__username"))[0][0]
            else:
                raise forms.ValidationError("邀请码错误，请重新输入")


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50,required=True,
                               widget=forms.TextInput(attrs={'class':'form-control'}),
                               error_messages={'required':'用户名不能为空',
                                                'max_length':"用户名不能长于50字符"})
    password = forms.CharField(label='密码',max_length=20,
                               widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        filter_result = User.objects.filter(username__exact=username)
        if not filter_result:
            raise forms.ValidationError("用户名不存在")
        return username

class PwdChangeForm(forms.Form):
    def __init__(self, user,*args,**kwargs):
        self.user = user
        super().__init__(*args,**kwargs)

    # class Meta:
    password = forms.CharField(label='旧密码',max_length=20,
                               widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='新密码',max_length=20,
                               widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='确认新密码',max_length=20,
                               widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_password(self):
        password = self.cleaned_data.get('password')
        print(password)
        print(make_password(password))
        if list(User.objects.filter(username__exact=self.user.username).values_list('password'))[0][0] != password:
            raise forms.ValidationError('原密码错误')
        return password

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 6:
            raise forms.ValidationError('密码太短')
        elif len(password1) > 20:
            raise forms.ValidationError('密码太长')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError('两次输入密码不一致')
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


class GoodsInfoForm(forms.Form):
    buy_date = forms.DateTimeField(label='购买日期',
                                   initial=datetime.date.today(),
                                   widget=forms.TextInput(attrs={'class':'form-control',
                                                                 'id':'datepicker'}))
    category = forms.ChoiceField(label="目类",
                                 choices=configs.GOODS_CATEGORY,
                                 widget=forms.Select(attrs={'class':'form-control'}))
    brand = forms.ChoiceField(label="品牌(填入新品牌后以后自动可以查询到)",
                               choices=(),
                               widget = forms.Select(attrs={'class':'form-control select2'}))

    style = forms.ChoiceField(label="款式",
                              choices=configs.GOODS_STYLE,
                              widget = forms.Select(attrs={'class':'form-control'}))

    name = forms.CharField(label="品名",max_length=128,
                           widget=forms.TextInput(attrs={'class':'form-control'}))

    sku = forms.CharField(label="编号",max_length=50,
                          widget=forms.TextInput(attrs={'class':'form-control'}))

    remark = forms.CharField(label= "商品备注",
                             required= False,
                             widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'rows':'2'}))

    def __init__(self,user,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.username = user.username
        self.fields['brand'].widget.choices = models.GoodsInfo.objects.filter(operator__exact=self.username).values_list('brand','brand')
        print(models.GoodsInfo.objects.filter(operator__exact=self.username))


class BuyInfoForm(forms.Form):
    size = forms.CharField(label= "尺码，不同用','隔开，也可以用*来表示多双，例如('XL*2,XXL*3'代表5个商品)）",
                           widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'rows':'3'}))

    ori_price=forms.CharField(label="价格(当地货币)/每个商品",
                             widget=forms.TextInput(attrs={'class':'form-control'}))

    taxes=forms.CharField(label="消费税率（例如税率为8.25%，填写为8.25即可）",
                             widget=forms.TextInput(attrs={'class':'form-control'}))

    exchange=forms.CharField(label="汇率（1当地货币=？人民币）",
                          widget=forms.TextInput(attrs={'class':'form-control'}))

    fees=forms.CharField(label="额外费用(例如小费等)/每个商品",
                         initial="0",
                             widget=forms.TextInput(attrs={'class':'form-control'}))

    nickname = forms.ChoiceField(label="购买者",
                              choices=(),
                              widget = forms.Select(attrs={'class':'form-control'}))

    def __init__(self,username,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.username = username
        self.fields['nickname'].widget.choices = models.BuyerWithSeller.objects.filter(username=self.username,status__exact="1").values_list('id','nickname')


class StoreInfoForm(forms.Form):
    country = forms.CharField(label='国家',
                              widget=forms.TextInput(attrs={'class':'form-control'}))
    store = forms.CharField(label="商店信息",
                            widget=forms.TextInput(attrs={'class':'form-control'}))

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['country'].initial = self.user.profile.country
        # print(self.fields['country'].widget.attrs)


class CreatTeamForm(forms.Form):
    choice = forms.ChoiceField(label="类型",
                               choices=configs.USER_STATIUS,
                               widget=forms.Select(attrs={'class':'form-control'}))
    nickname = forms.CharField(label='团队名',
                               widget=forms.TextInput(attrs={'class':'form-control'}))


class CreatTeamFormSub(forms.Form):
    username = forms.ChoiceField(label="用户名",
                                 widget=forms.TextInput(attrs={'class':'form-control'}))
    percentage = forms.ChoiceField(label="所占比例(直接一百内数字即可，代表百分比)",
                                   widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_percentage(self):
        percentage = self.cleaned_data.get('percentage')
        try:
            percentage = float(percentage)
        except:
            raise forms.ValidationError("百分比数字填写有误")
        return percentage


class ShipInterInfo(forms.Form):
    ship_store = forms.ChoiceField(label="快递公司",
                                   choices=configs.SHIP_COMCANY,
                                   widget=forms.Select(attrs={'class':'form-control'}))
    ship_number = forms.CharField(label="快递号",
                                  widget=forms.TextInput(attrs={'class':'form-control'}))
    ship_rmb = forms.CharField(label='快递费(rmb)',
                               initial=120,
                               widget=forms.TextInput(attrs={'class':'form-control'}))
    seller = forms.ChoiceField(label='收货人',
                               widget=forms.Select(attrs={'class':'form-control'}))

    def __init__(self,username,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['seller'].widget.choices=models.BuyerMatchSeller.objects.filter(buyer__username__exact=username).values_list("seller_id","seller__username")

    def clean_ship_rmb(self):
        ship_rmb = self.cleaned_data.get('ship_rmb')
        try:
            ship_rmb = float(ship_rmb)
        except:
            raise forms.ValidationError("邮寄费输入错误")
        return ship_rmb

    def clean_seller(self):
        seller = self.cleaned_data.get('seller')
        return seller


class SellInfoForm(forms.Form):
    platform = forms.ChoiceField(label="销售平台",
                                 choices=configs.SELL_PLATFORM_CHOICE,
                                 widget=forms.Select(attrs={'class':'form-control'}))
    sell_rmb = forms.CharField(label="销售价格",
                               widget=forms.TextInput(attrs={'class':'form-control'}))
    express_fee = forms.CharField(label="快递费",initial=15,
                               widget=forms.TextInput(attrs={'class':'form-control'}))
    final_rmb = forms.CharField(label="最终到账",
                               widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_sell_rmb(self):
        sell_rmb = self.cleaned_data.get('sell_rmb')
        try:
            sell_rmb = float(sell_rmb)
        except:
            raise forms.ValidationError("销售价格格式错误")
        return sell_rmb

    def clean_express_fee(self):
        express_fee = self.cleaned_data.get('express_fee')
        try:
            express_fee = float(express_fee)
        except:
            raise forms.ValidationError("快递费格式错误")
        return express_fee

    def clean_final_rmb(self):
        final_rmb = self.cleaned_data.get('final_rmb')
        try:
            final_rmb = float(final_rmb)
        except:
            raise forms.ValidationError("最终到账格式错误")
        return final_rmb

class BuyerMatchSeller(forms.Form):
    buyer = forms.ChoiceField(label="买方",
                               widget=forms.Select(attrs={'class':'form-control'}))
    seller = forms.ChoiceField(label="卖方",
                               widget=forms.Select(attrs={'class':'form-control'}))

    def __init__(self,buyer_name,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['buyer'].widget.choices = models.BuyerWithSeller.objects.filter(buyer__in=['buyer','admin'],
                                                                                    username__exact=buyer_name,
                                                                                    status='1').values_list("id","nickname")
        self.fields['seller'].widget.choices = models.BuyerWithSeller.objects.filter(buyer__in=['seller','admin'],
                                                                                  status='1').values_list('id','nickname')

    def clean_buyer(self):
        buyer = self.cleaned_data.get('buyer')
        seller = self.cleaned_data.get('seller')
        try:
            print(1)
            models.BuyerWithSeller.objects.get(id=buyer)
            print(2)
            models.BuyerWithSeller.objects.get(id=seller)
            print(3)
        except:
            raise forms.ValidationError("错误")
        return buyer
