from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout

# 登录处理
def signin( request):
    # 从 HTTP POST 请求中获取用户名、密码参数
    userName = request.POST.get('username')
    passWord = request.POST.get('password')

    # 使用 Django auth 库里面的 方法校验用户名、密码
    user = authenticate(username=userName, password=passWord)

    if user is None:
        return JsonResponse({'ret': 1, 'msg': '用户名或者密码错误'})
    if user.is_active:
        if user.is_superuser:
            login(request, user)
            # 在session中存入用户类型
            request.session['usertype'] = 'mgr'

            return JsonResponse({'ret': 0})
        else:
            return JsonResponse({'ret': 1, 'msg': '请使用管理员账户登录'})
    else:
        return JsonResponse({'ret': 0, 'msg': '用户已经被禁用'})


# 登出处理
def signout( request):
    # 使用登出方法
    logout(request)
    return JsonResponse({'ret': 0})
