# from django.conf.urls import include, url
# from django.contrib import admin

from django.conf.urls import url

from .views import (
  post_create_house,
  post_create_post,
  post_detail,
  post_list,
  post_update,
  post_delete,
  login,
  create_user,
  create_user_profile,
  post_list_roommate,
)

from .forms import QuestionnaireForm1, QuestionnaireForm2, QuestionnaireForm3
from .views import QuestionnaireWizard


urlpatterns = [
    url(r'^create_user/$', create_user),
    url(r'^create_user_profile/$', create_user_profile, name='user_profile'),
    url(r'^list/(?P<initial_city>\D+)$', post_list, name='list'),
    url(r'^list_roommate/(?P<initial_city>\D+)$', post_list_roommate, name='list_roommate'),
    ##remove name in list and list_roommate
    url(r'^list/$', post_list, name='list'),
    url(r'^list_roommate/$', post_list_roommate, name='list_roommate'),
    url(r'^create_house/$', post_create_house, name='create_house'),
    url(r'^create_post/(?P<house_id>\d+)$', post_create_post, name='create_post'),
    url(r'^(?P<post_id>\d+)/$', post_detail, name="detail"),
    url(r'^login/$', login, name="login"),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
    url(r'^questionnaire/$', QuestionnaireWizard.as_view([QuestionnaireForm1,
                                                          QuestionnaireForm2,
                                                          QuestionnaireForm3]),
                                                          name='questionnaire'),
]

