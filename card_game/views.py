from django.template import RequestContext
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.utils.http import urlquote
from django.utils.encoding import iri_to_uri
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from card_game.forms import CardForm
from card_game.models import Unique_Card,Card
from user_control.models import UserProfile
from django.contrib.auth.models import User
import urllib

# Create your views here.
def index(request):
    context = RequestContext(request)
    return render_to_response('card_game/index.html',{},context)

@login_required
def add_card(request):
    context = RequestContext(request)

    if request.method == 'POST':
        print request
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            tempuser = User.objects.get(username = request.user)
            card.change_author = UserProfile.objects.get(user = tempuser)
            #card.change_author = UserProfile.objects.get(user = request.user)
            card.save()
            uniquecard = Unique_Card()
            uniquecard.card_id = Card.objects.get(name=card.name)
            #print "DEBUG: ",card.name
            uniquecard.save()
            return render_to_response('card_game/add_card.html',{'form':CardForm,'message':'Card Added Successfully!'},context)

    return render_to_response('card_game/add_card.html',{'form':CardForm},context)

# @login_required
# def restricted(request):
#     return HttpResponse("This page is restricted")
