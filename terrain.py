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
from match.models import *
from video.models import *
from flow.models import *

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
    pass
    #world.browser.quit()


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
    assert text.lower() in world.browser.html.lower()

@step(u'I should not see the text "(.*)"')
def i_should_see_the_text(step, text):
    assert text.lower() not in world.browser.html.lower()

@step(u'I should see the tag "(.*)"')
def i_should_see_the_tag(step, tag):
    assert 'id="%s"' % tag in world.browser.html

@step(u'I should not see the tag "(.*)"')
def i_should_not_see_the_tag(step, tag):
    assert 'id="%s"' % tag not in world.browser.html

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
    for d in step.hashes:
        if not d.get('start'):
            d['start'] = None
        else:
            d['start'] = Technique.objects.get(name=d['start'])
        if not d.get('end'):
            d['end'] = None
        else:
            d['end'] = Technique.objects.get(name=d['end'])
        technique = Technique(**d)
        technique.save()

@step(u'Given I have the following videos in my database:')
def given_i_have_the_following_videos_in_my_database(step):
    Video.objects.all().delete()
    for video_dict in step.hashes:
        video = Video(**video_dict)
        video.save()

@step(u'Given I have the following matches in my database:')
def given_i_have_the_following_matches_in_my_database(step):
    Match.objects.all().delete()
    for match_dict in step.hashes:
        match = Match(**match_dict)
        match.save()

@step(u'Given I have the following flows in my database:')
def given_i_have_the_following_flows_in_my_database(step):
    Flow.objects.all().delete()
    for flow_dict in step.hashes:
        flow = Flow(**flow_dict)
        flow.save()

@step(u'Given the following flow relationship in my database:')
def given_the_following_flow_relationship_in_my_database(step):
    for d in step.hashes:
        f = Flow.objects.get(name = d['flow_name'])
        t = Technique.objects.get(name = d['technique_name'])
        f.techniques.add(t)
        f.save()

@step(u'Given the following relationship in my database:')
def given_the_following_relationship_in_my_database(step):
    for d in step.hashes:
        v = Video.objects.get(youtube_id = d['youtube_id'])
        t = Technique.objects.get(name = d['technique_name'])
        t.instructionals.add(v)
        t.save()

@step(u'I should see the video "(.*)"')
def i_should_see_the_video(step, youtube_id):
    assert youtube_id in world.browser.html

@step(u'I fill in "(.*)" with "(.*)"')
def i_fill_in(step, field, value):
    world.browser.fill(field, value)

@step(u'I select "(.*)" as technique "(.*)"')
def i_select_technique(step, field, value):
    #Todo: really need a generalized version of this
    value = Technique.objects.get(name=value).id
    world.browser.select(field, value)

@step(u'I submit the form "(.*)"')
def i_submit_the_form(step, form):
    world.browser.find_by_css('#%s .submit' % form).first.click()
