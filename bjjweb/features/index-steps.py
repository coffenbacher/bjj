from django.contrib.auth.models import User
from lettuce import *
from lettuce.django import django_url

@step(u'I go to the "(.*)" URL')
def i_go_to_the_url(step, url):
    print "testing"
    world.response = world.browser.visit(django_url(url))

@step(u'I should see (\d+) (\w+) tags')
def i_should_see_tags(step, n, tag):
    assert len(world.browser.find_by_css('img')) == 4

@step(u'I should see the header "(.*)"')
def i_should_see_the_header(step, header):
    assert header in world.browser.html

@step(u'I am logged in')
def i_am_logged_in(step):
    test = 't@t.com'
    User.objects.create_user(test, test, test)
    world.browser.visit(django_url('/'))
    world.browser.fill('username', test)
    world.browser.fill('password', test)
    world.browser.find_by_css('.submit').first.click()
     
