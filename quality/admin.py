from django.contrib import admin
import xadmin
from quality.models import *

class Late_matin_Admin(object):
    list_display = ('student', 'date', 'record_time', 'record_user', 'note')
    list_filter = ('date', )
    search_field = ('student', )


class Late_morn_exer_Admin(object):
    list_display = ('student', 'date', 'record_time', 'record_user', 'note')
    list_filter = ('date',)
    search_field = ('student',)


xadmin.site.register(Late_matin, Late_matin_Admin)
xadmin.site.register(Late_morn_exer, Late_matin_Admin)
