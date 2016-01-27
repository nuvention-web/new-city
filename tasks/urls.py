from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^categories/$', views.category_index, name='category_index'),
    # url(r'^questions/$', views.question_index, name='question_index')
    # url(r')
    # # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
