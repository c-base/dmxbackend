from django.conf.urls.defaults import patterns, include, url

from jsonrpc import jsonrpc_site
import dmxacl.lightSync.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dmxacl.views.home', name='home'),
    # url(r'^dmxacl/', include('dmxacl.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^json/', jsonrpc_site.dispatch)
)

