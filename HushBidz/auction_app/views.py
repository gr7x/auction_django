from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib import messages
from .models import Auction, Items
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
from .forms import AddItemForm, AddAuctionForm
from django.contrib.auth.decorators import login_required


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

@login_required()
def manage_auction(request):	
    auctions = Auction.objects.order_by('-start_time')
    context = {
        'auctions': auctions,
    }
    return render(request, 'auction_app/manage_auction.html', context)


@login_required()
def add_items(request): #, pk):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            parent_id = int(request.POST.get('parent_id'))
            item =form.save(commit=False)
            item.auction = Auction.objects.get(id=parent_id)
            #form.cleaned_data[]
            item.save()#request)
            return redirect('manage_auction')
        else: 
            print(form.errors)
    else: 
        form = AddItemForm()
    auction = get_object_or_404(Auction) #, pk=pk)
    context = {
    'auction': auction,
    }
    return render(request, 'auction_app/add_items.html', context)


@login_required()
def create_auction(request):
    template = loader.get_template('auction_app/setup_auction.html')
    context = {}
    if request.method == 'POST':
        form = AddAuctionForm(request.POST)
        form.admin = request.user.username
        if form.is_valid():
            post = form.save(commit=False)
            post.admin=request.user.username
            post.save()
            form.save()
            #form.cleaned_data[]
            return redirect('manage_auction')
        else: 
            print(form.errors)
        

    return HttpResponse(template.render(context,request))

@login_required()
def liveAuction(request):
    #if request.method == 'POST':

    return render(request, 'auction_app/liveAuction.html') #, {'form' : form})
         
