"""photofeed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from feed.views import * 

from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', index, name = 'index'),
    url(r'^push_feed$', push_feed),
    url(r'^pusher_authentication', pusher_authentication),
    url(r'^admin/', admin.site.urls),
    #url(r'^login/$', login),
    #url(r'^login/$',register),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('index/delete_feed/<int:id>/',delete_feed, name='delete_feed'),
        


]
