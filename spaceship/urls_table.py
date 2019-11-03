from django.urls import re_path
from . import views

app_name = 'spaceship'
urlpatterns = [
    re_path(r'^warehouse_in/search$',views.warehouse_in_search),
    re_path(r'^myShoes/myShoesChildTable$',views.my_shoes_child_table),

    re_path(r'^myShoes/$',views.my_shoes),
    re_path(r'^myShoes2/$',views.my_shoes2),
    re_path(r'^myShoes3/$',views.my_shoes3),
    re_path(r'^myShoes/myShoeTable$',views.my_shoes_table),
    re_path(r'^myShoes2/shiptochina$',views.my_shoes_table_ship_to_china),
    re_path(r'^myShoes2/readytosell$',views.my_shoes_table_ready_to_sell),

    re_path(r'^myShoes2/myShoeTable$',views.my_shoes_table2),
    re_path(r'^myShoes3/myShoeTable$',views.my_shoes_table3),
    re_path(r'^showGoodsDetail$',views.show_goods_detail),
]