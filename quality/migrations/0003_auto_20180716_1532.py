# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-16 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality', '0002_praiserecord_standard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='学期')),
            ],
            options={
                'verbose_name': '学期',
                'verbose_name_plural': '学期',
            },
        ),
        migrations.AlterField(
            model_name='praiserecord',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/praise', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='publishmentrecord',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/publish', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='student',
            name='account',
            field=models.CharField(blank=True, max_length=30, verbose_name='一卡通卡号'),
        ),
    ]