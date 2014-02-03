from django.template import RequestContext
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.utils.http import urlquote
from django.utils.encoding import iri_to_uri
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import urllib

# Create your views here.
def index(request):
    context = RequestContext(request)
    return HttpResponseRedirect('login/')
def user_login(request):
    context = RequestContext(request)

    if request.method == "POST":
        #Get username and password:
        username = request.POST['username']
        password = request.POST['password']

        #Is this a valid user?
        user = authenticate(username=username,password=password)

        #Check for a user object:
        if user is not None:
            #Make sure user has not been deactivated:
            if user.is_active:
                login(request,user)
                #return HttpResponse("temporary login landing page")
                return HttpResponseRedirect('/')
            else:
                return render_to_response('login.html',{'disabled_account':True},context)
        else:
            #print "Invalid login details: {0}".format(username)
            return render_to_response('login.html',{'bad_details':True}, context)
    else:
        #Return the login form:
        return render_to_response('login.html', {}, context)


@login_required
def user_logout(request):
    #we know the user is logged in thanks to the decorator, so we don't need to check:
    logout(request)
    #go back to the homepage:
    return HttpResponseRedirect('/')
