"""Primary_School_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import settings
from student_management_app import views, HodViews

urlpatterns = [
    path('', views.ShowLoginPage,name="show_login"),
    path('doLogin', views.doLogin,name="do_login"),
    path('get_user_deail', views.GetUserDetails),
    path('logout_user', views.logout_user, name="logout"),
    path('admin_home/', HodViews.admin_home,name="admin_home"),
    path('add_staff', HodViews.add_staff,name="add_staff"),
    path('add_staff_save', HodViews.add_staff_save,name="add_staff_save"),
    path('add_course', HodViews.add_course, name="add_course"),
    path('add_course_save', HodViews.add_course_save,name="add_course_save"),
    path('add_student', HodViews.add_student, name="add_student"),
    path('add_student_save', HodViews.add_student_save, name="add_student_save"),
    path('demo/', views.showDemoPage),
    path('admin/', admin.site.urls),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
