# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from tastypie.api import Api
from api import ProfileResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(ProfileResource())
v1_api.register(UserResource())

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.home),
    url(r'^run/', views.home),
    url(r'^view/(?P<dialogue_id>\d+)/(?P<page_number>\d+)/$', views.getDialogue),
    url(r'^view/(?P<dialogue_id>\d+)/$', views.getDialogue),
    url(r'^view/', views.view),
    url(r'^about/', views.about),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^api/', include(v1_api.urls)),

    url(r'^', views.home),
)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)