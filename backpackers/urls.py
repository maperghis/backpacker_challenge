from django.conf.urls import patterns, url
from backpackers import views

urlpatterns = patterns('',
    url(r'^person/$', views.PersonList.as_view()),
    url(r'^person/(?P<name>[a-zA-Z]+\s[a-zA-Z]+)/$',
        views.PersonDetail.as_view()),
    url(r'^state/$', views.StateList.as_view()),
    url(r'^state/(?P<name>[a-zA-Z]+)/$', views.StateDetail.as_view()),
    url(r'^transport/$', views.TransportList.as_view()),
    url(r'^transport/(?P<mode>[a-zA-Z]+)/$', views.TransportDetail.as_view()),
    )
