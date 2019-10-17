from django.apps import AppConfig
from django.forms.models import model_to_dict
from .authority import moduleAuthority
from .config import *
from .forms import newSKUform,newBought
from .models import PubSnkrsStyle


class SnkrsConfig(AppConfig):
    name = 'snkrs'

class FormSet(object):
    def __init__(self):
        self.newSKU_form = newSKUform
        self.newBought_form = newBought

class userItems(dict):
    def __init__(self,user):
        self.firstItems = {}
        self.item_index = self.get_items_index(user)
        for (k,v) in self.item_index.items():
            self.firstItems.update({ITEMS[k]:{ICON[k]:[ITEMS_DETAIL[k][m] for m in v]}})
    def get_items_index(self,user):
        #获取用户权限索引
        return  {'1':['1','2','3']}

class userInformation(object):
    def __init__(self,user):
        self.username = user
        self.news = self.get_news(user)
        self.newsNumber = len(self.news)
        self.alert = self.get_alert(user)
        self.alertNumber = len(self.alert)
        self.status = self.get_status(user)
        self.statusNumber = len(self.status)
        (self.userStatus,self.userStatusDetail) = self.get_user_status_info(self.get_user_status(user))
    def get_news(self,user):
        #获得消息
        return [1,2]
    def get_alert(self,user):
        #获得提示
        return [1,2]
    def get_status(self,user):
        #获得状态
        return [1,2]
    def get_user_status(self,user):
        #获取用户身份
        return 0
    def get_user_status_info(self,status):
        return USER_STATUS_INFO[status],USER_STATUS_INFO_DETAIL[status]

class User(object):
    def __init__(self,user):
        self.username = user
        self.item = userItems(user)
        self.infomation = userInformation(user)
        self.forms = FormSet()
        self.tem = self.get_tem()

    def get_newSKU_form_data(self,data):
        newSKU_form = self.forms.newSKU_form(data)
        if newSKU_form.is_valid():
            newSKU_form=newSKU_form.cleaned_data
            newSKU_form['Operator']=self.username
            (num,query) = get_data_from_pub_snkrs_style(newSKU_form['style_num'])
            if num > 0:
                self.set_inform(INFORM['newSKU']['failure'] + str(query))
            else:
                PubSnkrsStyle.objects.create(**newSKU_form)
                self.set_inform(INFORM['newSKU']['success'])
        else:
                self.set_inform(INFORM['newSKU']['failure'] + "others")

    def get_tem(self):
        tem = self._get_message()
        tem.update(self._get_module_items())
        print(tem)
        print(self._prepare_newSKU_message())
        tem.update(self._prepare_newSKU_message())
        return tem

    def set_inform(self, info):
        self.tem['inform'] = info

    def _get_message(self):
        return {'message':self.infomation}

    def _get_module_items(self):
        return {'auth':self.item}

    def _prepare_newSKU_message(self):
        return {'newSKUform':self.forms.newSKU_form()}

def get_User(username):
    if username in USER.keys():
        return USER[username]
    else:
        usr = User(username)
        USER.update({username:usr})
        return usr

def get_data_from_pub_snkrs_style(sku):
    query = PubSnkrsStyle.objects.filter(style_num=sku)
    num = query.count()
    return num, [model_to_dict(data) for data in query]
