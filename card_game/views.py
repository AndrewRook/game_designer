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
from django.forms.models import model_to_dict
import urllib

# Create your views here.
def index(request):
    context = RequestContext(request)
    return render_to_response('card_game/index.html',{},context)

# def testpage(request):
#     context = RequestContext(request)
#     return render_to_response('card_game/testpage.html',{},context)
# def testpagetwo(request):
#     context = RequestContext(request)
#     return render_to_response('card_game/testpage2.html',{},context)

def card_list(request):
    context = RequestContext(request)
    cardtypes = None
    firstcardform = None
    try:
        firstunique = Unique_Card.objects.all()[:1].get()
        firstcard = firstunique.card_id
        cardtypes = (firstcard)._meta.get_field('type').choices
        firstcardform = CardForm(model_to_dict(firstcard))
    except ObjectDoesNotExist:
        return render_to_response('card_game/card_list.html',{'cardtypes':None,'cardlist':None,'firstcardform':None},context)
    cardsbytype = []
    typenames = []
    for i in range(len(cardtypes)):
        typenames.append(cardtypes[i][1])
        uniquecards = Unique_Card.objects.filter(card_id__type__exact = cardtypes[i][0])
        cards_in_type = [CardForm(model_to_dict(card.card_id)) for card in uniquecards]
        cardsbytype.append(cards_in_type)

    return render_to_response('card_game/card_list.html',{'cardlist':zip(typenames,cardsbytype),'firstcardform':firstcardform},context)
    
    # current_card_list = Unique_Card.objects.all()
    # card_list = [CardForm(model_to_dict(card.card_id)) for card in current_card_list]
    # firstcard = None
    # card_types = None
    # if len(card_list) > 0:
    #     firstcard = card_list[0]
        
    # return render_to_response('card_game/card_list.html',{'cardlist':card_list,'firstcard':firstcard},context)

    
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

@login_required
def edit_card(request):
    context = RequestContext(request)
    return HttpResponse('Edit page goes here')
