# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-16 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quality', '0004_auto_20180716_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='空', verbose_name='评定内容')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quality.Student', verbose_name='学生')),
                ('term', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quality.Term', verbose_name='当前学期')),
            ],
            options={
                'verbose_name': '素质评定',
                'verbose_name_plural': '素质评定',
            },
        ),
        migrations.AlterField(
            model_name='praiserecord',
            name='image',
            field=models.ImageField(blank=True, upload_to='praise', verbose_name='图片'),
        ),
    ]
