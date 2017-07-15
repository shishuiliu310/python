from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import io
import time
from common import code as CheckCode
from user import models
# Create your views here.


def register(request):
    # 验证表单信息
    if request.method == 'POST':
        # 验证验证码是否正确
        session_code = request.session['CheckCode'].lower()
        code = request.POST['caption']
        if session_code == code:
            user_info = models.User(username=request.POST['username'],
                                    password=request.POST['password'],
                                    truename=request.POST['truename'],
                                    email=request.POST['email'],
                                    ctime=int(time.time()),
                                    last_login_ip=request.META['REMOTE_ADDR']
                                    )
            user_info.save()
            if user_info.id:
                request.session['username'] = request.POST['username']
                return HttpResponseRedirect('/index')
        return render(request, 'home/user/register.html')
    else:
        return render(request, 'home/user/register.html')


def login(request):

    # 显示登录页面
    if request.method == 'GET':

        # 将当期用户登录的页面存入到session中用于返回
        request.session['from'] = request.META.get('HTTP_REFERER', '/')
        return render(request, 'home/user/login.html')
    # 验证表单信息
    if request.method == 'POST':

        # 验证验证码是否正确
        session_code = request.session['CheckCode'].lower()
        code = request.POST['caption']
        if session_code == code:
            username = request.POST['username']
            password = request.POST['password']
            exist_user = models.User.objects.values('id', 'picture', 'intro').get(
                username=username, password=password, status=1)
            if exist_user:
                request.session['uid'] = exist_user['id']
                request.session['picture'] = exist_user['picture']
                request.session['intro'] = exist_user['intro']
                request.session['username'] = username
                return HttpResponseRedirect(request.session['from'])
        return HttpResponseRedirect('/index')


def loginout(request):
    try:
        del request.session['uid']
    except KeyError:
        pass

    return HttpResponseRedirect('/index')


def code(request):

    stream = io.BytesIO()
    # img图片对象,code在图像中写的内容
    img, code = CheckCode.create_validate_code(size=(90, 40))
    img.save(stream, "png")
    # 图片页面中显示,立即把session中的CheckCode更改为目前的随机字符串值
    request.session["CheckCode"] = code.lower()
    return HttpResponse(stream.getvalue())

    # 代码：生成一张图片，在图片中写文件
    # request.session['CheckCode'] =  图片上的内容

    # 自动生成图片，并且将图片中的文字保存在session中
    # 将图片内容返回给用户
