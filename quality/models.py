from django.db import models
from school_student.models import *
from datetime import date, datetime

class Late_matin(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=u'学生')
    date = models.DateField(u'迟到日期', default=date.today)
    record_time = models.DateTimeField(u'记录时间', default=datetime.now)
    record_user = models.CharField(u'记录人', max_length=100, blank=True)
    note = models.TextField(u'备注', default='', blank=True)

    def __str__(self):
        return self.student.student_name

    class Meta:
        verbose_name = '早课迟到'


class Late_morn_exer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=u'学生')
    date = models.DateField(u'迟到/缺勤日期', default=date.today)
    record_time = models.DateTimeField(u'记录时间', default=datetime.now)
    record_user = models.CharField(u'记录人', max_length=100, blank=True)
    note = models.TextField(u'备注', default='', blank=True)

    def __str__(self):
        return self.student.student_name

    class Meta:
        verbose_name = '早操迟到/缺勤'
