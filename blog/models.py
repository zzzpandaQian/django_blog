from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=20, verbose_name='类别名称')
    class Meta:
        db_table = 't_category'
        verbose_name_plural='类型'
    def __str__(self):
        return '%s'%self.cname

class Tag(models.Model):
    tname = models.CharField(max_length=20, verbose_name='标签名称')
    class Meta:
        db_table = 't_tag'
        verbose_name_plural = '标签'
    def __str__(self):
        return '%s'%self.tname

class P_ost(models.Model):
    pname = models.CharField(max_length=100, unique=True, verbose_name='标题')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='类别')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    desc = models.CharField(max_length=200, verbose_name='简述')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    isdelete = models.BooleanField(default=False, verbose_name='是否删除')
    content = RichTextUploadingField(null=True, blank=True, verbose_name='正文')
    class Meta:
        db_table = 't_post'
        verbose_name_plural = '帖子'

    def __str__(self):
        format = '%Y-%m-%d %H:%M:%S'
        self.created.strftime(format)
        return '%s%s'%(self.pname, self.created)