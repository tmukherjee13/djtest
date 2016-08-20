from django.conf.urls import patterns, include, url
from django.contrib import admin
from .landing import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'),
    url(r'download/^$', views.download_resume, name='download_resume'),
    
)
