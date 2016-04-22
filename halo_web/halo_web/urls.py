from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'halo_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
  
    url(r'^admin/', include(admin.site.urls)),
    url(r'^halo/',include('halo.urls', namespace = 'halo')),
    )
    
