from django.conf.urls import patterns, url
from backpackers import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    )
