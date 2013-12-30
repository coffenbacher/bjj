from django.conf.urls import patterns, url

urlpatterns = patterns('flow.views',
        url(r'^$', 'index'),
        url(r'^(?P<id>\d+)/$', 'show'),
        url(r'^(?P<id>\d+).json$', 'json'),
        url(r'^create/$', 'create'),
        )
