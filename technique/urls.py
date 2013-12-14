from django.conf.urls import patterns, url

urlpatterns = patterns('technique.views',
    url(r'^$', 'all'),
    url(r'^create/', 'create'),
    url(r'^(?P<id>\d+)/', 'show'),
    )
