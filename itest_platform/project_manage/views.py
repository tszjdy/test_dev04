from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def hello(request):
    return render(request,"hello.html")
def index(request):
    """
    实现登录
    """
    #返回登录页

    if request.method=="GET":
        return render(request,"index.html")
    #处理登录的数据
    if request.method =="POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        print("-->",username,password)
        user =auth.authenticate(username=username,password=password)
        print("-->",user)
       
        if username=="" or password =="":
            print("用户名密码不能为空")
            return render(request,"index.html",{"error": "username and password cannot be empty"})

        if user is not None:
            auth.login(request, user) #到数据库去写session_key
            return HttpResponseRedirect("/manage/")
        else:
            return render(request,"index.html",{"error":"Wrong user name and password!"})
@login_required #控制用户在未登录的情况下不能进入
def manage(request):
    """
    管理页面
    """
    return render(request,"manage.html")

# @login_required
def logout(request):
    """
    退出系统
    """
    auth.logout(request)
    return HttpResponseRedirect("/index/")