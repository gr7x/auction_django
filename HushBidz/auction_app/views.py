from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
#from .models import Auction, Item, Bid, User
#from .forms import DateForm

# Create your views here.
def register(request):
    template = loader.get_template('auction_app/register.html')
    context = {}
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('auction_app/index.html')
    context = {}
    return HttpResponse(template.render(context,request))

def manage_auction(request):
    template = loader.get_template('auction_app/manage_auction.html')	
    auctions = Auction.objects.order_by('-start_time')
    context = {
        'auctions': auctions,
        #deadline'now': time.strftime('%c'), 
    }
    return render(request, 'auction_app/manage_auction.html', context)


#def create_auction(request):
    #template = loader.get_template('setup_auction.html')
#    return render(request,'setup_auction.html')
