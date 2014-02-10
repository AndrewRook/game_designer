from django.conf.urls import patterns, url
from card_game import views
from django.http import HttpResponseRedirect
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^card_list/$', views.card_list, name='card list'),
                       url(r'^add_card/$', views.add_card, name='add card'),
                       url(r'^edit_card/(?P<card_id>\w+)/$', views.edit_card, name='edit card'),
                       # url(r'^testpage/$',views.testpage, name='test page'),
                       # url(r'^testpage2/$',views.testpagetwo, name='test page'),
                       )
