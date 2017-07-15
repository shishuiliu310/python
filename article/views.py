from django.shortcuts import render
from django.db.models import Count
from django.http import HttpResponseRedirect
from index import models

# Create your views here.


def article(request):
        # 获取当前的菜单
    article_id = request.GET.get('id')

    # 分类
    menu = models.Menu.objects.all().filter(status=1)
    # banner
    banner = models.Banner.objects.all().filter(status=1)
    # 文章
    # try:
    # 当前文章
    article = models.Article.objects.annotate(comment_num=Count('comment')
                                              ).get(pk=article_id, status=1)
    # 相关文章根据keyword关键字查询
    linkKeyword = article.keyword
    # 相关文章
    linkArticle = models.Article.objects.values('id', 'title', 'picture').filter(
        keyword=linkKeyword, status=1).exclude(pk=article.id).order_by("add_time")[0:6]
    # 上一篇文章
    upArticle = models.Article.objects.values('id', 'title').filter(
        pk__lt=article_id, status=1).order_by("-id")[0:1]
    # 下一篇文章
    downArticle = models.Article.objects.values('id', 'title').filter(
        pk__gt=article_id, status=1).order_by("id")[0:1]
    # 分类目录
    menuArticleNum = models.Article.objects.values('menu', 'menu__menuname').annotate(num=Count('menu')).filter(
        status=1)
    # 文章热搜
    hotArticle = models.Article.objects.all().filter(
        status=1).order_by("-hot")[0:10]
    # 热搜tag
    tagArticle = models.Article.objects.values('tag').annotate(num=Count('tag')).filter(
        status=1)
    # 评论
    # 父级评论
    pcomment = models.Comment.objects.values('id', 'content', 'reply_id', 'comment_time', 'user', 'user__picture', 'user__username').filter(
        article_id=article_id, reply_id=0).order_by("comment_time")[0:6]
    # 子级评论
    for index in range(len(pcomment)):
        ccomment = models.Comment.objects.values('content', 'reply_id', 'comment_time', 'user', 'user__picture', 'user__username').filter(
            reply_id=pcomment[index]['id']).order_by("comment_time")[0:10]
        pcomment[index]['son'] = ccomment
    print(pcomment)
    return render(request, 'home/article/article.html', {
        'menu': menu,
        'banner': banner,
        'article': article,
        'linkArticle': linkArticle,
        'upArticle': upArticle,
        'downArticle': downArticle,
        'hotArticle': hotArticle,
        'tagArticle': tagArticle,
        'menuArticleNum': menuArticleNum,
        'pcomment': pcomment,
    })
    # except:
    #     return HttpResponseRedirect('/index')
