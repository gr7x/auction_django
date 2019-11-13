from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib import messages
from .models import Auction
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
from .forms import AddItemForm, AddAuctionForm

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save(request)
            messages.success(request,'Account created successfully')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form})

def logout_view(request):
    logout(request)
    return redirect('index')

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
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        print("hi")
        if form.is_valid():
            print("oh")
            item =form.save(commit=False)
            #form.cleaned_data[]
            item.save()#request)
        return redirect('manage_auction')
    return render(request, 'auction_app/add_items.html', context)



def create_auction(request):
    template = loader.get_template('auction_app/setup_auction.html')
    context = {}
    if request.method == 'POST':
        form = AddAuctionForm(request.POST)
        if form.is_valid():
            auction = form.save(commit=False)
            #form.cleaned_data[]
            form.save()#request)
        return redirect('manage_auction')

    return HttpResponse(template.render(context,request))


def liveAuction(request):
    template = loader.get_template('auction_app/liveAuction.html')
    #if request.method == 'POST':

    return render(request, 'auction_app/liveAuction.html') #, {'form' : form})
         
