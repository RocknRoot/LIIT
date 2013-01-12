from django.conf.urls import patterns, include, url
import admin.urls
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LIIT.views.home', name='home'),
    # url(r'^LIIT/', include('LIIT.foo.urls')),
    url(r'^admin/', include(admin.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
