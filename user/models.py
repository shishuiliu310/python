from django.db import models
# Create your models here.


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
