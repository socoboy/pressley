from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^status/', 'sources.views.status_list'),
    url(r'^source/(?P<source_id>\d+)/', 'sources.views.source_history', name="source-history"),

    # Examples:
    # url(r'^$', 'pressley.views.home', name='home'),
    # url(r'^pressley/', include('pressley.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
