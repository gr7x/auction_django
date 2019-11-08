from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Auction
from .forms import CreateUserForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User

def signup(request):
    if request.user.is_authenticated:
        print('You\'re already authenticated???')
        return redirect('index')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save(request)
            messages.success(request,'Account created successfully')
            return redirect('index')
    else:
        form = CreateUserForm()
    return render(request, 'accounts/signup.html', {'form' : form})

def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if (user is not None and default_token_generator.check_token(user, token)):
        user.is_active = True
        user.save()
        messages.add_message(request, messages.INFO, 'YEEHAW! Account activated. Please login.')
    else: 
        messages.add_message(request, messages.INFO, 'WELL I\'LL BE DARNED. Link Expired. Contact admin to activate your account.')
 
    return redirect('accounts/login')

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
         
