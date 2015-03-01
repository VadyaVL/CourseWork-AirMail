from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

from rest_framework.urlpatterns import format_suffix_patterns
import api

#from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.home),
    url(r'^run/', views.home),
    url(r'^view/(?P<dialogue_id>\d+)/(?P<page_number>\d+)/$', views.getDialogue),
    url(r'^view/(?P<dialogue_id>\d+)/$', views.getDialogue),
    url(r'^view/', views.view),
    url(r'^about/', views.about),
    url(r'^auth/', include('loginsys.urls')),

    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/dialogues/$', api.DialogueList.as_view()),
    url(r'^api/dialogues/(?P<pk>\d+)/$', api.DialogueDetail.as_view()),
    #url(r'^', views.home),
)

urlpatterns = format_suffix_patterns(urlpatterns)