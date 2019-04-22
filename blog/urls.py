# coding=utf-8
from django.urls import re_path

from blog import views

routes = [
    re_path('^$', views.base),
    re_path('^page/(\d+)$', views.base),
    re_path('^post/(\d+)$', views.detail.as_view()),
    re_path('^category/(\d+)$', views.category),
    re_path('^archive/(\d+)/(\d+)$', views.archive),
    re_path('^archive/$', views.archive),

]