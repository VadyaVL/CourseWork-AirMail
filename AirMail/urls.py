from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

from rest_framework.urlpatterns import format_suffix_patterns
import api
from django.conf.urls import include


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.home),
    url(r'^run/', views.home),
    url(r'^view/(?P<dialogue_id>\d+)/(?P<page_number>\d+)/$', views.getDialogue),
    url(r'^view/(?P<dialogue_id>\d+)/$', views.getDialogue),
    url(r'^view/', views.view),
    url(r'^about/', views.about),
    url(r'^auth/', include('loginsys.urls')),


    url(r'^users/$', api.UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/$', api.UserDetail.as_view()),
    url(r'^info/$', api.InformationList.as_view()),
    url(r'^info/(?P<pk>\d+)/$', api.InformationDetail.as_view()),
    url(r'^dialogues/$', api.DialogueList.as_view()),
    url(r'^dialogues/(?P<pk>\d+)/$', api.DialogueDetail.as_view()),

    #url(r'^', views.home),
)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

