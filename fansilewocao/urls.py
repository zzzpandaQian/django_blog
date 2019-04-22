"""fansilewocao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import haystack
from django.contrib import admin
from django.db import InternalError
from django.urls import path, include, re_path
from django.views.static import serve

from blog.urls import routes
from fansilewocao.settings import DEBUG, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routes)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('search/', include('haystack.urls'))
]

if DEBUG:
    urlpatterns += re_path('^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),