from django.conf.urls import patterns, url, include
from backpackers import views
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
