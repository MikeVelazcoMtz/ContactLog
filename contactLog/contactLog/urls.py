# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'contactLog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('apps.contact.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pretty/', TemplateView.as_view(template_name='pretty.html'), name="pretty"),
)
