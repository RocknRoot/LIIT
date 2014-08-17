from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'liit.views.home', name='home'),
    # url(r'^liit/', include('liit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^login/$', 'auth.views.ulogin'),
    (r'^logout/$', 'auth.views.ulogout'),
    (r'^register/$', 'structure.views.user.register'),
    (r'^home/$', 'structure.views.user.index'),
)
