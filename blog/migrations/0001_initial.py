# Generated by Django 2.1.4 on 2019-04-17 21:33

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=20, verbose_name='类别名称')),
            ],
            options={
                'verbose_name_plural': '类型',
                'db_table': 't_category',
            },
        ),
        migrations.CreateModel(
            name='P_ost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100, unique=True, verbose_name='标题')),
                ('desc', models.CharField(max_length=200, verbose_name='简述')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('isdelete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='正文')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='类别')),
            ],
            options={
                'verbose_name_plural': '帖子',
                'db_table': 't_post',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=20, verbose_name='标签名称')),
            ],
            options={
                'verbose_name_plural': '标签',
                'db_table': 't_tag',
            },
        ),
        migrations.AddField(
            model_name='p_ost',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='标签'),
        ),
    ]
