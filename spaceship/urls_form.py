from django.urls import re_path
from . import views

app_name = 'spaceship'
urlpatterns = [
    re_path(r'^warehouse_in/search$',views.warehouse_in_search),
    re_path(r'^warehouse_in/$',views.warehouse_in),
]