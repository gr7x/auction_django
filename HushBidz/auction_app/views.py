from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Auction

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form})

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

def liveAuction(request):
    template = loader.get_template('auction_app/liveAuction.html')
    #if request.method == 'POST':

    return render(request, 'auction_app/liveAuction.html') #, {'form' : form})
         
