# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
import views

urlpatterns = patterns('forum.views',
        url(r'^list/(?P<slug>.+)/(?P<page>[0-9]*)$', views.list, name='forum-list'),
        url(r'^read/(?P<id>[0-9]+)$', views.read, name="forum-read"),
        url(r'^edit/(?P<id>[0-9]+)$', views.edit, name="forum-edit"),
        url(r'^write/(?P<slug>.+)$', views.write, name="forum-write"),
        url(r'^delete/(?P<id>[0-9]+)$', views.delete, name="forum-delete"),
        )

