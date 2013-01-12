from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    ## Status configuration
    url(r'^status/$', 'admin.views.status_index'),
    url(r'^status/add/$', 'admin.views.status_add'),
    url(r'^status/create/$', 'admin.views.status_create'),
    url(r'^status/(?P<status_id>\d+)/edit/$', 'admin.views.status_edit'),
    url(r'^status/(?P<status_id>\d+)/update/$', 'admin.views.status_update'),

    ## Type configuration
    url(r'^type/$', 'admin.views.type_index'),
    url(r'^type/add/$', 'admin.views.type_add'),
    url(r'^type/create/$', 'admin.views.type_create'),
    url(r'^type/(?P<type_id>\d+)/edit/$', 'admin.views.type_edit'),
    url(r'^type/(?P<type_id>\d+)/update/$', 'admin.views.type_update'),

    ## Workflow configuration
    url(r'^workflow/$', 'admin.views.workflow_index'),
    url(r'^type/(?P<type_id>\d+)/workflow/$', 'admin.views.workflow_edit'),
    url(r'^type/(?P<type_id>\d+)/workflow/update$', 'admin.views.workflow_update'),

)
