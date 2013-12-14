from lettuce import *
from nose.tools import assert_equal, assert_greater
from splinter.browser import Browser
from django.test.utils import setup_test_environment, teardown_test_environment
from django.core.management import call_command
from django.db import connection
from django.conf import settings
from lettuce.django import django_url

from video.models import *

@step(u'I go to the URL of video with id "(\w+)"')
def i_go_to_the_url_of_video(step, youtube_id):
    v = Video.objects.get(youtube_id=youtube_id)
    url = '/video/%s/' % v.id #Todo: clean this up using helper
    world.response = world.browser.visit(django_url(url))
