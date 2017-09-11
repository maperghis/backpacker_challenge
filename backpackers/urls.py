#!/usr/bin/env python
"""
:created on: 31-08-2017
:modified on: 11-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
from backpackers import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'state', views.StateViewSet)
router.register(r'transport', views.TransportViewSet)


urlpatterns = patterns('',
    url(r'^person/$', views.PersonList.as_view()),
    url(r'^person/(?P<name>[a-zA-Z]+\s[a-zA-Z]+)/$',
        views.PersonDetail.as_view()),
    url(r'^', include(router.urls)),
    )
