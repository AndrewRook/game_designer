from django.conf.urls import patterns, url
from card_game import views
from django.http import HttpResponseRedirect
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       )
