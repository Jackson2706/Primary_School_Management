from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from student_management_app.EmailBackEnd import EmailBackEnd


# Create your views here.
def showDemoPage(request):
    return render(request,template_name="demo.html")

def ShowLoginPage(request):
    return render(request,template_name="login_page.html")

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method is not allowed<h2>")
    else:
        user= authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user != None:
            login(request,user)
            return HttpResponse("Email: " + request.POST.get("email") + " Password: " + request.POST.get("password"))
        else:
            return HttpResponse("Error!")

def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User: " + request.user.email + " Usertype: " + request.user.user_type)
    else:
        return HttpResponse("please, login first!")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")