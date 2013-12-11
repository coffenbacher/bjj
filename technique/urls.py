from django.conf.urls import patterns, url

urlpatterns = patterns('technique.views',
    url(r'^(?P<id>\d+)/', 'show'),
    )
