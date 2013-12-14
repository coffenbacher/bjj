from django.conf.urls import patterns, url

urlpatterns = patterns('video.views',
        #url(r'^$', 'all'),
        url(r'^(?P<id>\d+)/$', 'show'),
        )
