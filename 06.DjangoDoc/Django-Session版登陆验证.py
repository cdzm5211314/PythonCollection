# 登陆验证装饰器
from functools import wraps
def check_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        next_url = request.get_full_path()
        if request.session.get("user"):
            return func(request, *args, **kwargs)
        else:
            return redirect("/login/?next={}".format(next_url))
    return inner

# 登陆
def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        if user == "alex" and pwd == "alex1234":
            # 设置session
            request.session["user"] = user
            # 获取跳到登陆页面之前的URL
            next_url = request.GET.get("next")
            # 如果有，就跳转回登陆之前的URL
            if next_url:
                return redirect(next_url)
            # 否则默认跳转到index页面
            else:
                return redirect("/index/")
    return render(request, "login.html")


# 退出
@check_login
def logout(request):
    # 删除所有当前请求相关的session
    request.session.delete()
    return redirect("/login/")


@check_login
def index(request):
    current_user = request.session.get("user", None)
    return render(request, "index.html", {"user": current_user})