from django.conf.urls import patterns, url

urlpatterns = patterns('match.views',
        url(r'^$', 'index'),
        url(r'^(?P<id>\d+)/$', 'show'),
    )
