# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('',

    url(r'^contact/$', views.ContactView.as_view(), name='go_contact'),
)
