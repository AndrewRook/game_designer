from django.conf.urls import patterns, url
from user_control import views
from django.http import HttpResponseRedirect
from django.conf import settings

def logout_required(view):
    def f(request, *args, **kwargs):
        if request.user.is_anonymous():
                return view(request, *args, **kwargs)
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return f

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^register/$',logout_required(views.register),name='register'),
                       url(r'^login/$', logout_required(views.user_login), name='login'),
                       #url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$',views.user_logout, name='logout'),
                       )
