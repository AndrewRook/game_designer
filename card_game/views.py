from django.template import RequestContext
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.utils.http import urlquote
from django.utils.encoding import iri_to_uri
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from card_game.forms import CardForm
import urllib

# Create your views here.
def index(request):
    context = RequestContext(request)
    return render_to_response('card_game/index.html',{},context)

def add_card(request):
    context = RequestContext(request)

    return render_to_response('card_game/add_card.html',{'form':CardForm},context)

# @login_required
# def restricted(request):
#     return HttpResponse("This page is restricted")
