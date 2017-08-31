from django.conf.urls import patterns, url
from backpackers import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^person/$', views.personList, name='personList'),
    url(r'^person/(?P<name>[a-zA-Z]+\s[a-zA-Z]+)/$', views.personDetail, name='personDetail')
    )
