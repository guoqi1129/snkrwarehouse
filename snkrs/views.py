from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .forms import LoginForm,newSKUform,newBought
from .apps import get_User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
import json

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                get_User(request.user.username)
                return HttpResponseRedirect("/index")
            else:
                return render(request, 'account/login.html', {"form":login_form, "next": "app.index"})

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'common/login.html',{"form":login_form,"next":"app.index"})

@login_required
def home_page(request):
    usr = get_User(request.user.username)
    return render(request, "app/index.html", usr.tem)

@login_required
def newSKUhtml(request):
    usr = get_User(request.user.username)
    if request.method == "POST":
        usr.get_newSKU_form_data(request.POST)
        return HttpResponse(json.dumps({"1":2},ensure_ascii=False),content_type="application/json,charset=utf-8")
    if request.method == "GET":
        usr.set_inform("")
        return render(request, 'app/forms/newSKU.html', usr.tem)


@login_required
def bought_new(request):
    usr = get_User(request.user.username)
    usr.set_inform("")
    if request.method == "POST":
        usr.set_new_bought_form_data(request.POST)
        return render(request, 'app/forms/bought.html', usr.tem)
    if request.method == "GET":
        return render(request, 'app/forms/bought.html', usr.tem)

@login_required
def warehouse_in(request):
    usr = get_User(request.user.username)
    usr.get_tem()
    if request.method == 'GET':
        return render(request, 'app/warehouse/warehouse_in.html', usr.tem)