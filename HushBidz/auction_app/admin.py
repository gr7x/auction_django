from django.contrib import admin
from .models import User
from .models import Auction
from .models import Items
# Register your models here.

admin.site.register(User)
admin.site.register(Auction)
admin.site.register(Items)
