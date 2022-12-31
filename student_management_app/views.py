from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render



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
            print(user.user_type, type(user.user_type))
            if user.user_type == "1":
                return HttpResponseRedirect('admin_home')
            elif user.user_type == "2":
                return HttpResponse('staff login')
            else:
                return HttpResponse('student login')
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponse("Error!")

def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User: " + request.user.email + " Usertype: " + request.user.user_type)
    else:
        return HttpResponse("please, login first!")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")