from django.shortcuts import render
from django.http import HttpResponse

from common.models import Customer


def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息。。。")

def listcustomers(request):
    # 返回一个QuerySet对象，包含所有的表记录
    # 每条表记录都是一个字典对象，key是字段名，value是字段值
    qs = Customer.objects.values()
    ret_str = ''
    for customer in qs:
        for name, value in customer.items():
            ret_str += f'{name}:{value} | '
            # <br>表示换行
        ret_str += '<br>'

    return HttpResponse(ret_str)