from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AirMail.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.home),
    url(r'^run/', views.home),
    url(r'^view/(?P<dialogue_id>\d+)/(?P<page_number>\d+)/$', views.getDialogue),
    url(r'^view/(?P<dialogue_id>\d+)/$', views.getDialogue),
    url(r'^view/', views.view),
    url(r'^about/', views.about),
    url(r'^auth/', include('loginsys.urls')),


    url(r'^', views.home),
)
