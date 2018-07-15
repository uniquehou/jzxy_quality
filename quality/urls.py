from django.conf.urls import url, include
from quality.views import *

app_name = 'quality'
urlpatterns = [
    url(r'^$', Search.as_view(), name='search'),
    url(r'^search/$', Search.as_view(), name='search'),
    url(r'^venify/$', verify, name='venify'),     # 验证学号
    url(r'^addinfo/$', AddInfo.as_view(), name='addinfo'),    # 补全信息
    url(r'^se_account/$', SeAccount.as_view()),    # 查找饭卡
]
