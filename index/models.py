from django.db import models

# Create your models here.


class Menu(models.Model):
    topid = models.IntegerField()
    sortrank = models.IntegerField()
    menuname = models.CharField(max_length=9)
    englishname = models.CharField(max_length=9)
    status = models.SmallIntegerField()
    title = models.CharField(max_length=80)
    keyword = models.CharField(max_length=40)
    description = models.CharField(max_length=200)

    class Meta:
        db_table = "blog_menu"


class Banner(models.Model):
    url = models.CharField(max_length=255, verbose_name='图片链接')
    banner = models.CharField(max_length=255)
    msg = models.CharField(max_length=255)
    status = models.SmallIntegerField()

    class Meta:
        db_table = "blog_banner"


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    menu = models.ForeignKey('Menu')
    add_time = models.IntegerField()
    picture = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    hot = models.IntegerField(default=0)
    love = models.IntegerField(default=0)
    status = models.SmallIntegerField()

    class Meta:
        db_table = "blog_article"


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=16, null=True)
    truename = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    intro = models.CharField(max_length=100)
    picture = models.CharField(max_length=200)
    ctime = models.IntegerField(null=True)
    last_login_ip = models.CharField(max_length=15)
    status = models.SmallIntegerField(default=1)
    login_num = models.IntegerField(default=0)

    class Meta:
        db_table = "blog_user"


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey('Article')
    reply_id = models.IntegerField(default=0)
    user = models.ForeignKey('User')
    content = models.CharField(max_length=255)
    comment_time = models.IntegerField(null=True)

    class Meta:
        db_table = "blog_comment"