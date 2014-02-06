from django.template import RequestContext
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.utils.http import urlquote
from django.utils.encoding import iri_to_uri
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import urllib

from user_control.forms import UserForm,UserProfileForm


# Create your views here.
def index(request):
    context = RequestContext(request)
    return HttpResponseRedirect('login/')

def register(request):
    context = RequestContext(request)

    #Was registration successful? Defaults to false:
    registered = False

    #Check if POST request:
    if request.method == 'POST':
        #Grab information from /both/ user form and user profile form:
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        #If valid, sign them up!
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            #Hash the password:
            user.set_password(user.password)
            user.save()

            #Check out the UserProfile. since we need to set the user attribute we can't save things right away:
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    print context
    return render_to_response('user_control/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered}, context)

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
                return HttpResponseRedirect('/')
            else:
                return render_to_response('user_control/login.html',{'disabled_account':True},context)
        else:
            #print "Invalid login details: {0}".format(username)
            return render_to_response('user_control/login.html',{'bad_details':True}, context)
    else:
        #Return the login form:
        return render_to_response('user_control/login.html', {}, context)


@login_required
def user_logout(request):
    #we know the user is logged in thanks to the decorator, so we don't need to check:
    logout(request)
    #go back to the homepage:
    return HttpResponseRedirect('/')
