# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 23:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Late_matin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='迟到日期')),
                ('record_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='记录时间')),
                ('record_user', models.CharField(blank=True, max_length=100, verbose_name='记录人')),
                ('note', models.TextField(blank=True, default='', verbose_name='备注')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_student.Student', verbose_name='学生')),
            ],
            options={
                'verbose_name': '早课迟到',
            },
        ),
        migrations.CreateModel(
            name='Late_morn_exer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='迟到/缺勤日期')),
                ('record_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='记录时间')),
                ('record_user', models.CharField(blank=True, max_length=100, verbose_name='记录人')),
                ('note', models.TextField(blank=True, default='', verbose_name='备注')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_student.Student', verbose_name='学生')),
            ],
            options={
                'verbose_name': '早操迟到/缺勤',
            },
        ),
    ]