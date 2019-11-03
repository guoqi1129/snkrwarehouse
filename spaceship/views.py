from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile,BuyerWithSeller
from django.contrib import auth
from .forms import (RegistrationForm, LoginForm, update_country,
                    PwdChangeForm,GoodsInfoForm,BuyInfoForm,
                    StoreInfoForm,CreatTeamForm,CreatTeamFormSub,
                    ShipInterInfo,SellInfoForm,BuyerMatchSeller)

from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
import random,string
from . import configs
from .apps import get_User
from django.contrib.auth.decorators import login_required

from django.forms import formset_factory
from django.core import serializers

# Create your views here.


def get_invite_code():
    code = "".join(map(str,[random.choice(string.ascii_letters+string.digits) for i in range(6)])).upper()
    while UserProfile.objects.filter(invite_code__exact=code).count() >0:
        code = "".join(map(str,[random.choice(string.ascii_letters+string.digits) for i in range(6)])).upper()
    return code


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            country = form.cleaned_data.get('country')
            telephone = form.cleaned_data.get('telephone')
            user_groups = form.cleaned_data.get('user_groups')
            invite_people = form.cleaned_data.get('invite_people')
            names = form.cleaned_data.get('names')
            alipay = form.cleaned_data.get('alipay')
            user = User.objects.create_user(username=username,password=password,email=email)
            user = User.objects.get(username=user)
            UserProfile.objects.create(user=user,country=country,telephone=telephone,user_status='active',
                                        user_groups=user_groups,email=email,names=names,invite_code=get_invite_code(),
                                        invite_people=invite_people,alipay=alipay,special_sign1="买卖要公平",special_sign2="我思故我在")
            user = get_User(username)
            user.team.save({'choice':user_groups,'nickname':username})
            if country not in configs.COUNTRY_LIST:
                update_country()
            return HttpResponseRedirect(reverse('spaceship_account:login'))
        else:
            return render(request, 'account/register.html', {"form":form})
    else:
        form = RegistrationForm()
        return render(request, 'account/register.html', {"form":form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:     #success
                auth.login(request, user)
                get_User(username)
                return HttpResponseRedirect(reverse('spaceship_main:index'))
            else:   #failed
                return render(request,'account/login.html',{'form':form,
                                                           'inform':'密码错误，请再试一次'})
        else:
            return render(request,'account/login.html',{'form':form})
    else:
        form = LoginForm()
        return render(request, 'account/login.html',{"form":form})


@login_required
def pwd_change(request):
    inform = None
    usr = get_User(request.user.username)
    if request.method == 'GET':
        form = PwdChangeForm(usr)
        tem = usr.tem
        tem.update({'form':form})
        return render(request,'account/pwd_change.html',tem)
    else:
        form = PwdChangeForm(usr,request.POST)
        print(form.is_valid())
        tem = usr.tem
        tem.update({'form':form})
        return render(request,'account/pwd_change.html',tem)

def logout(request):
    pass

@login_required
def creat_team(request):
    inform = None
    usr = get_User(request.user.username)
    if request.method == 'GET':
        form_creat_team = CreatTeamForm()
        return creat_team_return(request,usr,form_creat_team)
    else:
        form_num = int((len(request.POST)-3)/2+1)  #team用户数
        form_creat_team = CreatTeamForm(request.POST)
        keys = [v for v in request.POST][3:len(request.POST)]
        username_list = []
        percentage_list = []
        try:
            for i in range(form_num):
                if i%2==0:
                    userna=request.POST.get(keys[i])
                    username_list.append(userna)
                    User.objects.get(username__exact=userna)
                else:
                    percentage_list.append(float(request.POST.get(keys[i])))
            if sum(percentage_list) >= 100:
                return creat_team_return(request,usr,form_creat_team,inform="百分比分配有误")
            if len(username_list)>len(set(username_list)):

                return creat_team_return(request,usr,form_creat_team,inform="不能有重复用户名")

        except:
            return creat_team_return(request,usr,form_creat_team,inform="填写的用户和百分比有误")
        usr.team.save(request.POST,username_list,percentage_list)
        return creat_team_return(request,usr,form_creat_team,inform="添加成功，请等待相关用户确认后团队生效")

def creat_team_return(request,usr,form_creat_team,inform=None,title="团队创建"):
    tem = usr.tem
    tem.update({"title":title})
    if inform is not None:
        tem.update({"inform":inform})
    tem.update({'form_creat_team':form_creat_team})
    return render(request,'account/creat_team.html',tem)


@login_required
def warehouse_in(request):
    inform = None
    usr = get_User(request.user.username)
    if request.method == 'GET':
        tem = usr.warehouse_in_return()
        return render(request,'spaceship/warehouse/warehouse_in.html',tem)
    else:       #处理新增数据
        data = usr.warehouse_in_save(request)
        tem = usr.warehouse_in_return(data)
        return render(request,'spaceship/warehouse/warehouse_in.html',tem)



@login_required
def index(request):
    usr = get_User(request.user.username)
    if request.method == 'GET':
        return render(request, 'spaceship/index.html', usr.tem)


@login_required
def warehouse_in_search(request):
    usr = get_User(request.user.username)
    keywords = request.POST.get("searchs")
    if keywords is None:
        return JsonResponse({"error": "搜索关键字错误"})
    else:
        data = usr.warehouse_in_search(keywords)
        if len(data)==0:
            return JsonResponse({"error": "搜索不到结果"})
        else:
            return JsonResponse(list(data),safe=False)

@login_required
def my_shoes(request):
    usr = get_User(request.user.username)
    tem = usr.tem
    if request.method =='GET':
        form_ship_info=ShipInterInfo(usr.username)
        tem.update({'title':"入库后发货",'form_ship_info':form_ship_info})
        return render(request, 'spaceship/table/myShoes.html', usr.tem)
    else:
        form_ship_info = ShipInterInfo(usr.username)
        try:
            float(request.POST.get('ship_rmb'))
        except:
            tem.update({'title':"入库后发货",'inform':'数据错误','form_ship_info':form_ship_info})
            return render(request, 'spaceship/table/myShoes.html', usr.tem)
        tem.update(usr.ship_my_shoes(request.POST))
        tem.update({'title':"入库后发货",'form_ship_info':form_ship_info})
        return render(request, 'spaceship/table/myShoes.html', usr.tem)


@login_required
def my_shoes2(request):
    usr = get_User(request.user.username)
    if request.method =='GET':
        tem = usr.tem
        tem.update({'title':"收货和上架"})
        return render(request, 'spaceship/table/myShoes2.html', usr.tem)
    else:
        form_ship_info = ShipInterInfo(usr.username,request.POST)
        if form_ship_info.is_valid():
            form_ship_info=ShipInterInfo(usr.username)
            tem = usr.tem
            tem.update(usr.ship_my_shoes(request.POST))
            tem.update({'title':"收货和上架",'form_ship_info':form_ship_info})
        return render(request, 'spaceship/table/myShoes2.html', usr.tem)


@login_required
def my_shoes3(request):
    usr = get_User(request.user.username)
    if request.method =='GET':
        form_sell_info = SellInfoForm()
        tem = usr.tem
        tem.update({'title':"销售和归档",'form_sell_info':form_sell_info})
        return render(request, 'spaceship/table/myShoes2.html', usr.tem)
    else:
        pass


@login_required
def my_shoes_table(request):
    user=get_User(request.user.username)
    if request.method=='GET':
        data = user.get_my_shoe_table('1')
        return JsonResponse(list(data),safe=False)


@login_required
def my_shoes_table_ship_to_china(request):
    usr=get_User(request.user.username)
    if request.method=='POST':
        id = request.POST.get('id')
        key = request.POST.get('action')
        tem = usr.update_status(key,id)
        print(tem)
        usr.set_inform(tem['inform'])
        return JsonResponse(list(tem),safe=False)


@login_required
def my_shoes_table_ready_to_sell(request):
    usr=get_User(request.user.username)
    if request.method=='POST':
        id = request.POST.get('id')
        tem = usr.update_status("read_to_sell",id)
        print(tem)
        return JsonResponse(list(tem),safe=False)


@login_required
def my_shoes_table2(request):
    user=get_User(request.user.username)
    if request.method=='GET':
        data = user.get_my_shoe_table('2')
        print(len(data))
        return JsonResponse(list(data),safe=False)


@login_required
def my_shoes_table3(request):
    user=get_User(request.user.username)
    if request.method=='GET':
        data = user.get_my_shoe_table('3')
        print(len(data))
        print(len(list(data)))
        return JsonResponse(list(data),safe=False)


@login_required
def my_shoes_child_table(request):
    user = get_User(request.user.username)
    if request.method=='POST':
        print(1)
        data = user.get_my_shoe_child_table(request.POST)
        return JsonResponse(list(data),safe=False)


@login_required
def show_goods_detail(request):
    usr = get_User(request.user.username)
    tem = usr.tem
    return render(request,'spaceship/base_main.html',tem)



@login_required
def match_team(request):
    usr = get_User(request.user.username)
    tem = usr.make_match_team_tem()
    if request.method == 'GET':
        return render(request,'account/match_team.html',tem)
    else:
        tem.update(usr.match_team_save(request.POST.get('buyer'),request.POST.get('seller')))
        return render(request,'account/match_team.html',tem)

