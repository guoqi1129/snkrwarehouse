USER = {}
AUTH_STATUS = {"1":"admin","2":"buyer","3":"seller"}
ITEMS = {"1":"仓库管理","2":"查询数据"}
ITEMS_DETAIL= {"1":{'1':'库存新增','2':'买到鞋了','3':'卖出鞋啦'},
               "2":{"4":"我的鞋","5":'我的钱'}}
ICON = {"1":"fa-edit","2":"fa-table"}
USER_STATUS_INFO = ['富婆包养者']
USER_STATUS_INFO_DETAIL = ['富婆包养我，有钱霍霍霍']
ITEM_URLS = {
    "库存新增": "/index/warehouse_in.html",
    "买到鞋了": "/index/forms/bought.html",
    "卖出鞋啦": "/index/forms/sold.html",
    "我的鞋":"/index/query/myShoes.html",
    "我的钱":"/index/query/myMoney.html",
}
SHOE_STYLE=["男","女","大童","小童"]

INFORM = {
    "newSKU":{"failure":"添加失败:","success":"添加成功"},
}
GOODS_STATUS={"1":'已登记入仓库',
              "2":'发往国内',
              "3":'国内已经收货',
              "4":'国内已上架',
              '5':'已经卖出',
              '6':'已经归档'}