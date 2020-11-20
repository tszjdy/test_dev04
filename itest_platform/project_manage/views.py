from django.shortcuts import render
from django.http import HttpResponse
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
        if username=="" or password =="":
            print("用户名密码不能为空")
            return render(request,"index.html",{"error": "username and password cannot be empty"})

        if username=="admin" and password=="123456":
            return render(request,"index.html",{"error":"login success!"})
        else:
            return render(request,"index.html",{"error":"Wrong user name and password!"})
