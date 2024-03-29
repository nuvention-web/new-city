"""newcity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
# from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import TemplateView

from .views import (
    home,
    user_profile_detail,
    create_user_profile,
    my_profile_detail,
    my_matches,
    test_template,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^posts/', include("posts.urls", namespace="posts")),
    url(r'^users/(?P<user_profile_id>\d+)$', user_profile_detail, name= "user_profile_detail"),
    url(r'^users/create_user_profile/', create_user_profile, name= "create_user_profile"),
    url(r'^profile', my_profile_detail, name="my_profile_detail"),
    url(r'^matches', my_matches, name="my_matches" ),
    url(r'^test/',test_template),
    url(r'^login', TemplateView.as_view(template_name="login.html")),
    url(r'^logout', TemplateView.as_view(template_name="logout.html")),
    url(r'^accounts/', include('allauth.urls')),
]
