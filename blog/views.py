from django.shortcuts import render

# Create your views here.
from django.views import View

from blog.models import *
from django.core.paginator import Paginator

def base(request, num=1):
    postlist = P_ost.objects.all()
    pagelist = Paginator(postlist, 1)
    pageunit = pagelist.page(num)

    return render(request, 'index.html',{'pgobj': pagelist, 'page': pageunit})


class detail(View):
    def get(self,request, id):
        postid = int(id)
        # obj = P_ost.objects.filter(id=postid)[0]
        obj = P_ost.objects.get(id=postid)  # 也可以
        return render(request, 'detail.html', {'obj': obj})


def category(request, num):
    poli = P_ost.objects.filter(category_id=num)
    return render(request, 'postlist.html', {'poli': poli})


def archive(request, year=0, month=0):
    if not year and not month:
        poli = P_ost.objects.all()
    else:
        poli = P_ost.objects.filter(created__year=year, created__month=month)


    return render(request, 'postlist.html', {'poli': poli})