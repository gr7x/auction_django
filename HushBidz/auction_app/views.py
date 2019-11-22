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
from .forms import AddItemForm, AddAuctionForm, PostForm
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
    auctions = Auction.objects.all()
    context = {
        'auctions': auctions,
    }
    template = loader.get_template('auction_app/index.html')
    return HttpResponse(template.render(context,request))

@login_required()
def manage_auction(request):	
    auctions = Auction.objects.all()
    context = {
        'auctions': auctions,
    }
    return render(request, 'auction_app/manage_auction.html', context)


@login_required()
def add_items(request, pk):

    auction = get_object_or_404(Auction, pk=pk)
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            #parent_id = int(request.POST.get('parent_id'))
            item = form.save(commit=False)
            item.auction = auction#Auction.objects.get(id=parent_id)
            #form.cleaned_data[]
            item.save()
            return redirect('add_items', pk=auction.pk)#parent_id)
        else: 
            print(form.errors)
    else: 
        form = AddItemForm()
    items = auction.items.all()
    context = {
    'auction': auction,
    'items': items,
    'form': form,
    }
    return render(request, 'auction_app/add_items.html', context)


@login_required()
def create_auction(request):
    template = loader.get_template('auction_app/setup_auction.html')
    #contest = {}
    if request.method == 'POST':
        form = AddAuctionForm(request.POST)
        form.admin = request.user.username
        if form.is_valid():
            #form.cleaned_data[]
            post = form.save(commit=False)
            post.admin=request.user.username
            post.save()
            return redirect('manage_auction')
        else: 
            print(form.errors)
    else:
        form = AddAuctionForm()
    context = {
        'form': form
    }       
    return HttpResponse(template.render(context,request))

@login_required()
def liveAuction(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            #parent_id = int(request.POST.get('parent_id'))
            item = form.save(commit=False)
            #item.blog = Blog.objects.get(id=parent_id)
            item.save()
            return redirect('liveAuction')
    else:
        form = PostForm()
    auctions = Auction.objects.all()

    return render(request, 'auction_app/liveAuction.html', {'auctions' : auctions}) #'form' : form, 

@login_required()
def view_item(request, pk, id):
    auction = get_object_or_404(Auction, pk=pk)
    items   = auction.items.all()
    print(items)
    item = get_object_or_404(Items, id=id)
    context = {
            'item': item
    }
    return render(request, 'auction_app/view_item.html', context)

@login_required()
def place_bid(request, pk, id): 
    if request.method == 'POST':
       # form = AddItemForm(request.POST)
        #if form.is_valid():
        itemx = get_object_or_404(Items, id=id)
        item=Items.objects.get(name=request.Post['item_name'])  ## replace with id
        item.highest_bidder = request.user.username
        item.price = request.POST['price']
        #form.cleaned_data[]
        item.save()
        return redirect('auction_page')
    else: 
        print(form.errors)
    return render(request, 'auction_app/auction_page.html', context)



 
@login_required()
def view_auction(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    items = auction.items.all()
    context = {
    'auction': auction,
    'items': items,
    }
    return render(request, 'auction_app/view_auction.html', context)         
