from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from landing.models import Portfolio

class PortfolioSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        #return Portfolio.objects.all()
        return ['home']

    def location(self, item):
        return reverse(item)
      
