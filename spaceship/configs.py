COUNTRY_LIST = None
USER_STATUS = {'buyer':'买家','seller':'卖家'}
USER_STATIUS = tuple(USER_STATUS.items())

ITEMS_USER = {
    "admin":['11','12','13','31','32','33','51','91','92','93'],
    'buyer':['11','12','31','32','51','91','92'],
    'seller':['13','31','32','51','91','92'],
}
ITEMS_DETAIL= {"仓库管理":{
                        "fa-edit":{
                            '11':'库存新增',
                            '12':'买到鞋了',
                            '13':'卖出鞋啦'}},
                "状态管理":{
                        "fa-server":{
                            "31":"入库后邮寄",
                            "32":'收货和上架',
                            "33":'销售和归档',}},
                "信息管理":{
                        "fa-info-circle":{
                            "51":"消息中心"
                        }},
                "用户管理":{"fa-user":{
                            "91":'修改密码',
                            "92":'团队创建',
                            "93":'团队匹配',
                        }}}
ITEM_URLS = {
    "11": "/form/warehouse_in",
    "12": "/form/bought",
    "13": "/form/sold",
    "31": "/table/myShoes",
    "32": "/table/myShoes2",
    "33": "/table/myShoes3",
    '51': '/info/infoCenter',
    "91": "/account/pwdchange",
    "92": "/account/creat_team",
    '93': "/account/match_team",
}

USERS={}

GOODS_CATEGORY = (("鞋","鞋"),
                  ("包","包"),
                  ("简单衣裤","简单衣裤"),
                  ("外套/大衣","外套/大衣"),
                  ("电器/化妆品","电器/化妆品"),
                  ("香水/首饰","香水/首饰"),
                  ("手表","手表"),
                  ('保健品/食品/奶粉','保健品/食品/奶粉'),
                  ('食品粉剂/液体/洗护/生活用品','食品粉剂/液体/洗护/生活用品'))
GOODS_STYLE = (("男","男"),("女","女"),("儿童","儿童"),("婴儿","婴儿"))

TEAM_NEWS={"creat_news":"src_name向您提出了创建choice团队nickname的申请，你的占比为percentage%"}

WAREHOUSE_STATUS = {'1':'已入库',
                    '2':'回国中',
                    '3':'国内入库',
                    '4':'国内上架',
                    '5':'国内卖出',
                    '6':'已到账',
                    '7':'已归档'}

SHIP_COMCANY_DICT = {'西游寄':'西游寄',
                '其它':'其它'}
SHIP_COMCANY = tuple(SHIP_COMCANY_DICT.items())

SELL_PLATFORM_CHOICE=(("毒","毒"),("Nice","Nice"),("其它","其它"))