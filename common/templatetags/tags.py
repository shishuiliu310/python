from django import template
import time
register = template.Library()

# 注册时间戳转化为日期格式


@register.filter(name='timestampToDate')
def timestampToDate(value):
    # 将时间戳转化为数组
    timeArray = time.localtime(value)
    # 将数组转化日期格式
    date = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    if date:
        return date
    else:
        return ''
