from django import forms
from .models import PubShoeBrand
from .config import SHOE_STYLE


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',widget=forms.TextInput(attrs={'class':'form-row'}))
    password = forms.CharField(label='密码',widget=forms.PasswordInput(attrs={'class':'form-row'}))


class newSKUform(forms.Form):
    style_num = forms.CharField(max_length=20,
                                error_messages={'max_length':'最多20字符'},
                                label= "SKU码（必填）最多20字符",
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'palceholder':'XXXXXX-XXX'}))
    style_name = forms.CharField(max_length=30,
                                 error_messages={'max_length':'最多20字符'},
                                 label="船名（必填）",
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    brand = forms.ChoiceField(choices=PubShoeBrand.objects.all().values_list('brand','brand'),
                              widget=forms.Select(attrs={'class':'form-control select2',
                                                         'style':'width: 100%;'}),label="品牌")
    style = forms.ChoiceField(choices=((b,b) for b in SHOE_STYLE),
                              widget=forms.Select(attrs={'class':'form-control select2',
                                                         'style':'width: 100%;'}),
                              label="款式")
    remark = forms.CharField(label='备注',
                             max_length=50,
                             required=False,
                             widget=forms.Textarea(attrs={'class':'form-control',
                                                          'rows':'2'}))


class newBought(forms.Form):
    style_num = forms.CharField(max_length=20,
                                error_messages={'max_length':'最多20字符'},
                                label= "SKU码（必填）最多20字符",
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'palceholder':'XXXXXX-XXX'}))
    size = forms.CharField(label= "鞋码（多双用','隔开）",
                           widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'rows':'3'}))
    ori_price = forms.FloatField(label="价格（外币）",
                                   widget=forms.FloatField())
    exchange_rate = forms.FloatField(label="汇率",
                                       initial="7.08",
                                       widget=forms.TextInput(attrs={'class':'form-control'}))
