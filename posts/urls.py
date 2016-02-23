# from django.conf.urls import include, url
# from django.contrib import admin

from django.conf.urls import url

from .views import (
  home,
  post_create_house,
  post_create_post,
  post_details,
  post_list,
  post_update,
  post_delete,
  create_user,
)

urlpatterns = [
    url(r'^$', home),
    url(r'^create_user/$', create_user),
    url(r'^list/$', post_list, name='list'),
    url(r'^create_house/$', post_create_house, name='create_house'),
    url(r'^create_post/(?P<house_id>\d+)$', post_create_post, name='create_post'),
    #url(r'^(?P<id>\d+)/$', post_details, name="details"),
    url(r'^detail/$', post_detail),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
]

