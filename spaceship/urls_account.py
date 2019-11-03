from django.urls import re_path
from . import views

app_name = 'users'
urlpatterns = [
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^login/$',views.login, name='login'),
    re_path(r'^pwdchange/$',views.pwd_change,name='pwd_change'),
    re_path(r'^creat_team/$',views.creat_team,name='creat_team'),
    re_path(r'^match_team/$',views.match_team,name='match_team'),
    re_path(r'^index/$',views.logout,name='logout'),
]