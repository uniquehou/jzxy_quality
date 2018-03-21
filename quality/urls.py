from django.conf.urls import url, include
from quality.views import *

app_name = 'quality'
urlpatterns = [
    url(r'^search/$', Search.as_view(), name='search'),
]