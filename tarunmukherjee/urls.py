from django.conf.urls import patterns, include, url
from django.contrib import admin
from landing import views

from landing.sitemaps import PortfolioSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'portfolio': PortfolioSitemap(),
}

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'),
    url(r'resume/', views.resume, name='resume'),
    url(r'^postContact', views.contact, name='contact'),
    url(r'^backend/', include(admin.site.urls)),

    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap')
)
