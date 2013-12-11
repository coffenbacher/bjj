# terrain.py
import pdb
from lettuce import *
from nose.tools import assert_equal, assert_greater
from splinter.browser import Browser
from django.test.utils import setup_test_environment, teardown_test_environment
from django.core.management import call_command
from django.db import connection
from django.conf import settings

from django.contrib.auth.models import User
from technique.models import *

@before.harvest
def initial_setup(server):
    call_command('syncdb', interactive=False, verbosity=0)
    call_command('flush', interactive=False, verbosity=0)
    call_command('loaddata', 'all', verbosity=0)
    setup_test_environment()
    world.browser = Browser('chrome')

@after.harvest
def cleanup(server):
    connection.creation.destroy_test_db(settings.DATABASES['default']['NAME'])
    #teardown_test_environment()

@before.each_scenario
def reset_data(scenario):
    # Clean up django.
    call_command('flush', interactive=False, verbosity=0)
    call_command('loaddata', 'all', verbosity=0)

@after.all
def teardown_browser(total):
    world.browser.quit()


@step(u'I go to the "(.*)" URL')
def i_go_to_the_url(step, url):
    from lettuce.django import django_url
    world.response = world.browser.visit(django_url(url))

@step(u'I should see at least (\d+) (\w+) tags')
def i_should_see_tags(step, n, tag):
    assert_greater(len(world.browser.find_by_css('img')), int(n))

@step(u'I should see the header "(.*)"')
def i_should_see_the_header(step, header):
    assert header in world.browser.html

@step(u'I should see the text "(.*)"')
def i_should_see_the_text(step, text):
    assert text in world.browser.html

@step(u'I should see "(.*)" in the HTML')
def i_should_see_the_header(step, text):
    assert text in world.browser.html

@step(u'I am logged in')
def i_am_logged_in(step):
    from lettuce.django import django_url
    test = 't@t.com'
    User.objects.create_user(test, test, test)
    world.browser.visit(django_url('/'))
    world.browser.fill('username', test)
    world.browser.fill('password', test)
    world.browser.find_by_css('.submit').first.click()

@step(u'I have the following techniques in my database:')
def i_have_the_following_techniques(step):
    Technique.objects.all().delete()
    for technique_dict in step.hashes:
        technique = Technique(**technique_dict)
        technique.save()
