from django.conf.urls import include, url
from django.contrib import admin

from .views import (
  home,
  post_create_house,
  post_create_post,
  post_detail,
  post_list,
  post_update,
  post_delete,
  create_user,
)

urlpatterns = [
    url(r'^$', home),
    url(r'^create_user/$', create_user),
    url(r'^list/$', post_list),
    url(r'^create_house/$', post_create_house),
    url(r'^create_post/$', post_create_post),
    url(r'^detail/$', post_detail),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
]

