# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-16 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='院系名')),
            ],
            options={
                'verbose_name': '院系',
                'verbose_name_plural': '院系',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='班级名')),
            ],
            options={
                'verbose_name': '班级',
                'verbose_name_plural': '班级',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='专业名')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quality.Department', verbose_name='所属院系')),
            ],
            options={
                'verbose_name': '专业',
                'verbose_name_plural': '专业',
            },
        ),
        migrations.CreateModel(
            name='Praise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='素质拓展类型')),
            ],
            options={
                'verbose_name': '素质拓展类型',
                'verbose_name_plural': '素质拓展类型',
            },
        ),
        migrations.CreateModel(
            name='PraiseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=100, verbose_name='说明')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='补充说明')),
                ('image', models.ImageField(blank=True, upload_to='media/praise', verbose_name='图书')),
                ('praise_time', models.DateField(auto_now=True, verbose_name='时间')),
                ('praise_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quality.Praise', verbose_name='类型')),
            ],
            options={
                'verbose_name': '素质拓展记录',
                'verbose_name_plural': '素质拓展记录',
            },
        ),
        migrations.CreateModel(
            name='Publishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='违规违纪类型')),
            ],
            options={
                'verbose_name': '违规违纪类型',
                'verbose_name_plural': '违规违纪类型',
            },
        ),
        migrations.CreateModel(
            name='PublishmentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=100, verbose_name='说明')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='补充说明')),
                ('image', models.ImageField(blank=True, upload_to='media/publish', verbose_name='图书')),
                ('publish_time', models.DateField(auto_now=True, verbose_name='时间')),
                ('publish_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quality.Publishment', verbose_name='类型')),
            ],
            options={
                'verbose_name': '违规违纪记录',
                'verbose_name_plural': '违规违纪记录',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(default=' ', max_length=20, unique=True, verbose_name='学号')),
                ('password', models.CharField(default='96e79218965eb72c92a549dd5a330112', max_length=100, verbose_name='密码')),
                ('student_name', models.CharField(default=' ', max_length=30, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=1, verbose_name='性别')),
                ('nation', models.CharField(choices=[('1', '汉族'), ('2', '壮族'), ('3', '满族'), ('4', '回族'), ('5', '苗族'), ('6', '维吾尔族'), ('7', '土家族'), ('8', '彝族'), ('9', '蒙古族'), ('10', '藏族'), ('11', '布依族'), ('12', '侗族'), ('13', '瑶族'), ('14', '朝鲜族'), ('15', '白族'), ('16', '哈尼族'), ('17', '哈萨克族'), ('18', '黎族'), ('19', '傣族'), ('20', '畲族'), ('21', '傈僳族'), ('22', '仡佬族'), ('23', '东乡族'), ('24', '高山族'), ('25', '拉祜族'), ('26', '水族'), ('27', '佤族'), ('28', '纳西族'), ('29', '羌族'), ('30', '土族'), ('31', '仫佬族'), ('32', '锡伯族'), ('33', '柯尔克孜族'), ('34', '达斡尔族'), ('35', '景颇族'), ('36', '毛南族'), ('37', '撒拉族'), ('38', '布朗族'), ('39', '塔吉克族'), ('40', '阿昌族'), ('41', '普米族'), ('42', '鄂温克族'), ('43', '怒族'), ('44', '京族'), ('45', '基诺族'), ('46', '德昂族'), ('47', '保安族'), ('48', '俄罗斯族'), ('49', '裕固族'), ('50', '乌孜别克族'), ('51', '门巴族'), ('52', '鄂伦春族'), ('53', '独龙族'), ('54', '塔塔尔族'), ('55', '赫哲族'), ('56', '珞巴族')], default='1', max_length=2, verbose_name='民族')),
                ('political_satus', models.CharField(choices=[('1', '群众'), ('2', '共青团员'), ('3', '预备党员'), ('4', '共产党员'), ('5', '其它')], default='1', max_length=1, verbose_name='政治面貌')),
                ('duty', models.CharField(blank=True, default='', max_length=100, verbose_name='职务')),
                ('address', models.CharField(blank=True, default='', max_length=100, verbose_name='住址')),
                ('contact', models.CharField(blank=True, default='', max_length=20, verbose_name='本人联系方式')),
                ('parent_contact', models.CharField(blank=True, default='', max_length=20, verbose_name='亲属联系方式')),
                ('account', models.CharField(max_length=30, verbose_name='一卡通卡号')),
                ('student_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quality.Department', verbose_name='院系')),
                ('student_grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quality.Grade', verbose_name='班级')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
            },
        ),
        migrations.AddField(
            model_name='publishmentrecord',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quality.Student', verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='praiserecord',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quality.Student', verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='grade',
            name='major',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quality.Major', verbose_name='所属专业'),
        ),
    ]