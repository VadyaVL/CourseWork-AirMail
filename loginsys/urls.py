from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AirMail.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^register/', views.register),
)
