from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'',include('card_game.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user_control/', include('user_control.urls')),
    url(r'^card_game/', include('card_game.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}),
         )
