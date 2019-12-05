from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib import messages
from .models import Auction, Items
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
from .forms import AddItemForm, AddAuctionForm, PostForm, LivePostForm
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.db.models import Sum
from django.views.generic.edit import UpdateView
from datetime import datetime, timezone
from decimal import Decimal


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

@login_required
def admin_view(request):
    if request.user.is_superuser == False:
        return redirect('login')
    all_auctions = Auction.objects.all()
    context = {'all_auctions': all_auctions}

    return render (request, 'auction_app/admin_view.html', context)

@login_required
def admin_auction_view(request,pk):
    if request.user.is_superuser == False:
        return redirect('login')
    auction = get_object_or_404(Auction, pk=pk)
    items = auction.items.all()
    MEDIA_URL = '/auction_app'
    context = {
        'MEDIA_URL': MEDIA_URL,
        'items':items,
        }
    
    return render (request, 'auction_app/admin_auction_view.html',context)



@login_required()
def add_items(request, pk):

    auction = get_object_or_404(Auction, pk=pk)
    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.auction = auction
            #form.cleaned_data[]
            item.save()
            return redirect('add_items', pk=auction.pk)
        else: 
            print(form.errors)
    else: 
        form = AddItemForm()
    items = auction.items.all()
    #print(items)
    MEDIA_URL = '/auction_app'
    context = {
    'MEDIA_URL': MEDIA_URL,
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

@login_required
def live_view(request):
    if request.user.is_superuser == False:
        return redirect('login')
    all_auctions = Auction.objects.all()
    context = {'all_auctions': all_auctions}

    return render (request, 'auction_app/live_view.html', context)

@login_required()
def liveAuction(request, pk):
    if request.user.is_superuser == False:
        return redirect('login')
    form = LivePostForm(request.POST or None)
    if request.method == "POST":
        user_id = int(request.POST['highest_bidder'])
        user = User.objects.get(id=user_id)
        #user = get_object_or_404(User, pk=user_id)
        #user = User.get_by_id(user_id)
        if user:
            i_id = int(request.POST['i_id'])
            instance = Items.objects.get(id=i_id)
            form = LivePostForm(request.POST, instance=instance)
            if form.is_valid():
                item = form.save(commit=False)
                item.highest_bidder = user.username
                item.save()
                return redirect('liveAuction', pk=pk)
            else:
                print(form.errors)
        else:
            raise Http404("No matching user") 
    else:
        form = LivePostForm()
    auction = get_object_or_404(Auction, pk=pk)
    items   = auction.items.all()
    #item = get_object_or_404(Items, id=id)
    MEDIA_URL = '/auction_app'
    context = {
            'MEDIA_URL': MEDIA_URL,
            'auction': auction,
            'items': items,
            'form': form
    }

    return render(request, 'auction_app/liveAuction.html', context)

@login_required()
def view_item(request, pk, id):
    if request.method == "POST":
        instance = get_object_or_404(Items, id=id)
        form = PostForm(request.POST or None, instance=instance)
        if form.is_valid() and ValidTime(request, pk, id):
            postPrice = Decimal(request.POST['price'])
            if float(postPrice) > 0 and instance.price < float(postPrice): #and 
                item = form.save(commit=False)
                item.highest_bidder = request.user.username
                item.save()
                return redirect('view_item', pk=pk, id=id)        
            else:
                #raise Http404("Bid price was below the previous price")
                return redirect('view_item', pk=pk, id=id)
        else:
            raise Http404("This auction is not available")
            return redirect('view_item', pk=pk, id=id)
    else:
        form = PostForm()
    auction = get_object_or_404(Auction, pk=pk)
    items   = auction.items.all()
    item = get_object_or_404(Items, id=id)
    MEDIA_URL = '/auction_app'
    context = {
            'MEDIA_URL': MEDIA_URL,
            'auction': auction,
            'item': item,
            'form': form
    }
    return render(request, 'auction_app/view_item.html', context)

@login_required
def ValidTime(request, pk, id):
    auction = get_object_or_404(Auction, pk=pk) 
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
    MEDIA_URL = '/auction_app'
    context = {
    'MEDIA_URL': MEDIA_URL,
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
            for k in it:
                gandalf.append(getattr(auction, 'end_time'))
            items = items + list(chain(it))
        if pr['price__sum'] is not None:
            p = p + float(pr['price__sum'])
    items = zip(items, gandalf) 
    MEDIA_URL = '/auction_app'
    context = {
    'MEDIA_URL': MEDIA_URL,
    'tot_price': p,
    'auctions': auction,
    'items': items,
    'cur' : x,
    }
    return render(request, 'auction_app/user_page.html', context)      
