from school_student.models import *
import xadmin
from xadmin import views


class DepartmentAdmin(object):
    list_display = ('name', )
    search_fields = ('name', )


class MajorAdmin(object):
    list_display = ('name', )
    list_filter = ['department', ]
    search_fields = ('name', )


class GradeAdmin(object):
    list_display = ('name', )
    list_filter = ['major', ]
    search_fields = ('name', )


class StudentAdmin(object):
    list_display = ('student_id', 'student_name', 'student_department', 'student_major', 'student_grade')
    list_filter = ['student_department', 'student_grade']
    # readonly_fields = []
    search_fields = ('student_name', 'student_id')
    # raw_id_fields = ()
    # list_per_page = 20


class PraiseAdmin(object):
    list_display = ('student', 'praise_type', 'text', 'description', 'image', 'praise_time')
    list_filter = ('praise_time', 'praise_type')
    search_field = ('student', 'text')


class PublishAdmin(object):
    list_display = ('student', 'publish_type', 'text', 'description', 'image', 'publish_time')
    list_filter = ('publish_time', 'publish_type')
    search_field = ('student', 'text')


xadmin.site.register(Praise, PraiseAdmin)
xadmin.site.register(Publishment, PublishAdmin)


xadmin.site.register(Department, DepartmentAdmin)
xadmin.site.register(Major, MajorAdmin)
xadmin.site.register(Grade, GradeAdmin)
xadmin.site.register(Student, StudentAdmin)


class GlobalSetting(object):
    site_title = '晋中学院大学生素质记录'
    site_footer = '晋中学院'

xadmin.site.register(views.CommAdminView, GlobalSetting)
