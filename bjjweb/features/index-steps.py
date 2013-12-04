from lettuce import *
from lettuce.django import django_url

@step(u'I go to the "(.*)" URL')
def i_go_to_the_url(step, url):
    print "testing"
    world.response = world.browser.visit(django_url(url))

@step(u'I should see (\d+) (\w+) tags')
def i_should_see_tags(step, n, tag):
    print "test 2"
    assert False


@step(u'I should see the header "(.*)"')
def i_should_see_the_header(step, header):
    print "test 3"
    assert False
