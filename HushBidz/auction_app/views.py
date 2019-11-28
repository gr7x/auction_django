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
from itertools import chain
from django.db.models import Sum
from django.views.generic.edit import UpdateView
from datetime import datetime, timezone



class ItemUpdate(UpdateView):
    model = Items
    fields = ['highest_bidder', 'price']
    template_name_suffix = 'view_item'

class LiveItemUpdate(UpdateView):
    model = Items
    fields = ['highest_bidder', 'price']
    template_name_suffix = 'live_auction'

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
    print(items)
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
        form = LivePostForm(request.POST or None, instance=instance)
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
    instance = get_object_or_404(Items, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid() and ValidTime(request, pk, id):
        item = form.save(commit=False)
        item.highest_bidder = request.user.username
        form.save()
        return redirect('view_item', pk=pk, id=id)
    auction = get_object_or_404(Auction, pk=pk)
    items   = auction.items.all()
    item = get_object_or_404(Items, id=id)
    context = {
            'item': item,
            'form': form
    }
    return render(request, 'auction_app/view_item.html', context)

@login_required
def ValidTime(request, pk, id):
    auction = get_object_or_404(Auction, pk=id) 
    if getattr(auction, 'end_time') > datetime.now(timezone.utc) and getattr(auction, 'start_time') < datetime.now(timezone.utc):
        return True

    return False



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


@login_required()
def user_page(request):
    x = datetime.now(timezone.utc)
    usr = request.user.username 
    act =  Auction.objects.all().values_list('id', flat=True)
    items = []
    gandalf = []
    p = 0.00
    for id in act:
        auction = get_object_or_404(Auction, pk=id)
        it  = auction.items.all().filter(highest_bidder=usr)
        pr = auction.items.all().filter(highest_bidder=usr).aggregate(Sum('price'))      
        if it is not None:
            gandalf.append(getattr(auction, 'end_time'))
            items = items + list(chain(it))
        if pr['price__sum'] is not None:
            p = p + float(pr['price__sum'])
    items = zip(items, gandalf) 
    context = {
    'tot_price': p,
    'auctions': auction,
    'items': items,
    'cur' : x,
    }
    return render(request, 'auction_app/user_page.html', context)      
