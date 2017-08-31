from django.conf.urls import patterns, url
from backpackers import views

urlpatterns = patterns('',
    url(r'^person/$', views.personList, name='personList'),
    url(r'^person/(?P<name>[a-zA-Z]+\s[a-zA-Z]+)/$', views.personDetail,
        name='personDetail'),
    url(r'^state/$', views.stateList, name='stateList'),
    url(r'^state/(?P<name>[a-zA-Z]+)/$', views.stateDetail, name='stateDetail'),
    url(r'^transport/$', views.transportList, name='transportList'),
    url(r'^transport/(?P<mode>[a-zA-Z]+)/$', views.transportDetail,
        name='transportDetail'),
    )
