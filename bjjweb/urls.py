from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# http://stackoverflow.com/questions/38601/
def i18n_javascript(request):
    return admin.site.i18n_javascript(request)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bjjweb.views.index', name='index'),
    url(r'^login/$', 'bjjweb.views.log_in', name='log_in'),
    url(r'^flow/', include('flow.urls')),
    url(r'^match/', include('match.urls')),
    url(r'^video/', include('video.urls')),
    url(r'^technique/', include('technique.urls')),
    url(r'^admin/jsi18n', i18n_javascript),
    url(r'^admin/', include(admin.site.urls)),
)
