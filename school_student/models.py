from django.db import models

class Department(models.Model):
    name = models.CharField(u'院系名', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '院系'
        verbose_name_plural = '院系'


class Major(models.Model):
    department = models.ForeignKey("Department", models.SET_NULL, verbose_name=u'所属院系', null=True, blank=True)
    name = models.CharField(u'专业名', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '专业'
        verbose_name_plural = '专业'


class Grade(models.Model):
    major = models.ForeignKey("Major", on_delete=models.SET_NULL, verbose_name=u'所属专业', null=True, blank=True)
    name = models.CharField(u'班级名', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = '班级'


class Student(models.Model):

    student_name = models.CharField(u'姓名', max_length=30, default=' ')
    student_id = models.CharField(u'学号', max_length=20, default=' ', unique=True)
    student_major = models.ForeignKey("Major", on_delete=models.SET_NULL, verbose_name=u'专业', null=True, blank=True)
    student_department = models.ForeignKey("Department", on_delete=models.SET_NULL, verbose_name='院系', null=True, blank=True)
    student_grade = models.ForeignKey("Grade", on_delete=models.SET_NULL, verbose_name=u'班级', null=True, blank=True)

    def __str__(self):
        return self.student_name

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'