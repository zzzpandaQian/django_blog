# coding=utf-8

import datetime
from haystack import indexes
from blog.models import P_ost

# 类名格式为模型类名+Index
class P_ostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # 给模型类设置相关搜索内容的field
    pname = indexes.NgramField(model_attr='pname')
    content = indexes.NgramField(model_attr='content')

    def get_model(self):
        return P_ost  # 返回模型类

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.order_by('-created')