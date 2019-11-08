from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Auction, Items, User
#from .forms import DateForm

# Create your views here.
def register(request):
    template = loader.get_template('auction_app/register.html')
    context = {}
    if request.method == 'Post':
        # if request.Post.get('fullname') and request.Post.get('email') and request.Post.get('password')
            post = Post()
            post.fullname = request.Post.get('fullname')
            post.email = request.Post.get('email')
            post.password = request.Post.get('password')
            post.save()
            return HttpResponse(template.render(context, request))
    else:
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



def add_items(request):
    template = loader.get_template('auction_app/add_items.html')
    context = {}
    return HttpResponse(template.render(context,request))


def create_auction(request):
    template = loader.get_template('auction_app/setup_auction.html')
    context = {}
    if request.method == 'Post':
        if request.Post.get('auction_name') and request.Post.get('auction_type') and request.Post.get('start_Time') and request.Post.get('end_time'):
            post = Post()
            post.name = request.Post.get('auction_name')
            post.auction_type = request.Post.get('auction_type')
            post.start_time = request.Post.get('start_time')
            post.end_time = request.Post.get('end_time')
            post.save()
            return render(request, 'auction_app/add_items.html')
    else:
       return render(request, 'auction_app/setup_auction.html')
         
