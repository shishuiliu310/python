from django.shortcuts import render
from django.db.models import Count
from index import models
# 调用公共模块
from common.models import Common
# Create your views here.
import os

def index(request):

    # 分类
    menu = models.Menu.objects.all().filter(status=1)
    # banner
    banner = models.Banner.objects.all().filter(status=1)
    # 文章
    article = models.Article.objects.all().annotate(comment_num=Count('comment')
                                                    ).filter(status=1).order_by("-add_time")
    # 分页并获取分页数
    objects, page_range = Common.pagination(request, article)
    # 分类目录
    menuArticleNum = models.Article.objects.values('menu', 'menu__menuname').annotate(num=Count('menu')).filter(
        status=1)
    # 文章热搜
    hotArticle = models.Article.objects.all().filter(
        status=1).order_by("-hot")[0:10]
    # 热搜tag
    tagArticle = models.Article.objects.values('tag').annotate(num=Count('tag')).filter(
        status=1)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    return render(request, 'home/index/index.html', {
        'menu': menu,
        'banner': banner,
        'article': objects,
        'page_range': page_range,
        'hotArticle': hotArticle,
        'tagArticle': tagArticle,
        'menuArticleNum': menuArticleNum,
    })
