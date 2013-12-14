from django.conf.urls import patterns, url

urlpatterns = patterns('flow.views',
        url(r'^(?P<id>\d+)/$', 'show'),
        url(r'^create/$', 'create'),
        )
