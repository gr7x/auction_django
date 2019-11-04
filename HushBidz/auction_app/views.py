from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Auction
#from .forms import DateForm

# Create your views here.
def registrationConfirmation(request):
    template = loader.get_template('auction_app/registrationConfirmation.html')
    context = {}
    return HttpResponse(template.render(context,request))

@csrf_exempt
def registerUser(request):
    Auction.numUsers += 1
    fullName = request.POST.get('fullName',None),
    userNum  = Auction.numUsers
    Auction.users_set.create(fullName=fullName,
            email=request.POST.get('email',None),
            password=request.POST.get('password',None),
            number=userNum)
    template = loader.get_template('auction_app/registrationConfirmation.html')
    context = { 'userName' : fullName,
                'userNum'  : userNum }
    return HttpResponseRedirect(template.render(context, request))




@csrf_exempt
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


def create_auction(request):
    template = loader.get_template('setup_auction.html')
    return render(request,'setup_auction.html')
