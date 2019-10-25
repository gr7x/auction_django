from django.shortcuts import render
#from .models import Auction, Item, Bid, User
#from .forms import DateForm

# Create your views here.


def manage_auction(request):	
    #auctions = Auction.objects.order_by('-pub_date')
    #context = {
    #    'auctions': auctions,
    #    #deadline'now': time.strftime('%c'), 
    #}
    return render(request, 'auction_app/manage_auction.html')#, context)


#def create_auction(request):
    #template = loader.get_template('setup_auction.html')
#    return render(request,'setup_auction.html')
