from lettuce import *
from nose.tools import assert_equal, assert_greater
from splinter.browser import Browser
from django.test.utils import setup_test_environment, teardown_test_environment
from django.core.management import call_command
from django.db import connection
from django.conf import settings
from lettuce.django import django_url

from flow.models import *

@step(u'I go to the URL of flow with name "(\w+)"')
def i_go_to_the_url_of_flow(step, name):
    f = Flow.objects.get(name=name)
    url = '/flow/%s/' % f.id #Todo: clean this up using helper
    world.response = world.browser.visit(django_url(url))
