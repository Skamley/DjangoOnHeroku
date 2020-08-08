"""My_First_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from first_app import views
from django.conf.urls import include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^$', views.AppHomePage),
    #url(r'^$', views.index),
    url(r'^first_app/', include('first_app.urls')),
    #url(r'^$/', include('first_app.urls')),
    path('admin/', admin.site.urls),
    url(r'^.*Rock/$', views.rockUs, name="RockView"),
    url(r'^DemoView/', views.DemoView),
    url(r'^MyRegistration/', views.MyRegView, name="MyRegView"),
    #Following two lines are for rest framework
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))


]
