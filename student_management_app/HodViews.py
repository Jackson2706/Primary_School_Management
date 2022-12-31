import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse

from student_management_app.models import CustomUser, Course


def admin_home(request):
    return render(request, "hod_template/home_content.html")

def add_staff(request):
    return render(request, "hod_template/add_staff_template.html")

def add_staff_save(request):
    if request.method != "POST":
        return HttpResponse("Method is not allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(username=username, password=password,
                                                  email=email, last_name=last_name, first_name=first_name,
                                                  user_type=2)
            user.staffs.address=address
            user.save()
            messages.success(request, "Successfully added Staff")
            return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request,"Failed to add Staff")
            return HttpResponseRedirect(reverse("add_staff"))

def add_course(request):
    return render(request,"hod_template/add_course_template.html")

def add_course_save(request):
    if request.method != "POST":
        return HttpResponse("Method is not allowed")
    else:
        course = request.POST.get("course")
        try:
            course_model=Course(course_name=course)
            course_model.save()
            messages.success((request,"Successfully added course"))
            return HttpResponseRedirect(reverse('add_course'))
        except:
            messages.error(request,"Failed to added course")
            return HttpResponseRedirect(reverse('add_course'))

def add_student(request):
    courses = Course.objects.all()
    return render(request,"hod_template/add_student_template.html",{"courses":courses})

def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method is not allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        course_id = request.POST.get("course")
        sex = request.POST.get("sex")
        try:
            user = CustomUser.objects.create_user(username=username, password=password,
                                                  email=email, last_name=last_name, first_name=first_name,
                                                  user_type=2)
            user.students.address = address
            course_obj=Course.object.get(id=course_id)
            user.students.course_id = course_obj
            start_date = datetime.datetime.strptime(session_start,'%d-%m-%y').strptime("%Y-%m-%d")
            end_date = datetime.datetime.strptime(session_end, '%d-%m-%y').strptime("%Y-%m-%d")
            user.students.session_start_year = start_date
            user.students.session_end_year = end_date
            user.students.gender = sex
            user.students.profile_pic=''
            user.save()
            messages.success(request, "Successfully added Staff")
            return HttpResponseRedirect(reverse("add_student"))
        except:
            messages.error(request,"Failed to add Staff")
            return HttpResponseRedirect(reverse("add_student"))