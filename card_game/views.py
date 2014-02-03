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
    return render_to_response('index.html',{},context)
