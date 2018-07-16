from django.conf.urls import url, include
from quality.views import *

app_name = 'quality'
urlpatterns = [
    url(r'^$', Index.as_view(), name='default'),    # 首页
    url(r'^search/$', Search.as_view(), name='search'),
    url(r'^venify/$', verify, name='venify'),     # 验证学号
    url(r'^addinfo/$', AddInfo.as_view(), name='addinfo'),    # 补全信息
    url(r'^se_account/$', SeAccount.as_view()),    # 查找饭卡

    url(r'^login/$', Login.as_view(), name='login'),  # 登录
    url(r'^quit/$', quit, name='quit'),               # 退出
    url(r'^index/$', Index.as_view(), name='index'),  # 首页
    url(r'^info/$', Info.as_view(), name='info'),     # 个人信息
    url(r'^changepass/$', ChangePass.as_view(), name='changepass'),    # 修改密码
    url(r'^quality/$', Quality.as_view(), name='quality'),    # 素质记录
    url(r'^praise_info/$', praise_info, name='praise_info'),    # 素质拓展记录详细信息
    url(r'^publish_info/$', publish_info, name='publish_info')  # 违规违纪记录详细信息
]
