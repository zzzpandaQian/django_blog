# coding=utf-8
from django.db import connection
from django.db.models import Count

from blog.models import P_ost


def g_category(request):
    # 返回<QuerySet [('python', 1, 3), ('h5', 2, 1)]>
    cate = P_ost.objects.values_list('category__cname','category_id').annotate(c=Count("*")).order_by('-c')
    title_ = P_ost.objects.all()[0:3]
    cursor_ = connection.cursor()
    cursor_.execute('select count(*),year(created) ye,month(created) mo from t_post  group by ye,mo')
    creli = cursor_.fetchall() # 返回(('2019-04',4),)是元组类型。
    return {'cate': cate, 'title_':title_, 'creli': creli}