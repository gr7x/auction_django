from django.test import TestCase
from .models import Auction, Items
from django.utils import timezone
#from django.core.urlresolvers import reverse
from .forms import AddAuctionForm, AddItemForm

# Create your tests here.

class AuctionTest(TestCase):

# test models
    def create_auction(self, name="test", description="test", start_time=timezone.now(), end_time=(timezone.now() + timezone.timedelta(hours=1))):
        return Auction.objects.create(name=name, description=description, start_time=start_time, end_time=end_time)

    def test_auction_creation(self):
        w = self.create_auction()
        self.assertTrue(isinstance(w, Auction))
        #self.assertEqual(w.__unicode__(), w.name)

#test forms
    def test_valid_form(self):
        w = Auction.objects.create(name='Foo', description='Bar', start_time=timezone.now(), end_time=(timezone.now() + timezone.timedelta(hours=1)))
        data = {'name': w.name, 'description': w.description,  'start_time': w.start_time, 'end_time': w.end_time}
        form = AddAuctionForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = Auction.objects.create(name='Foo', description='',  start_time=timezone.now(), end_time=timezone.now())
        data = {'name': w.name, 'description': w.description, 'start_time': w.start_time, 'end_time': w.end_time}
        form = AddAuctionForm(data=data)
        self.assertFalse(form.is_valid())

#test views
#    def test_auction_list_view(self):
#        w = self.create_auction()
#        url = reverse("auction.views.auction")
#        resp = self.client.get(url)

#        self.assertEqual(resp.status_code, 200)
#        self.assertIn(w.name, resp.content)

class ItemTest(TestCase):

# test models

    a = Auction.objects.create(name='Foo', description='Bar',  start_time=timezone.now(), end_time=(timezone.now() + timezone.timedelta(hours=1)))
    a.save()
    def add_item(self, name="test", description="test", price=1, auction=a):
        return Items.objects.create(name=name, description=description, price=price, auction=auction)

    def test_item_creation(self):
        w = self.add_item()
        self.assertTrue(isinstance(w, Items))
        #self.assertEqual(w.__unicode__(), w.name)

#test forms
    def test_valid_form(self):
        a = Auction.objects.create(name='Foo', description='Bar',  start_time=timezone.now(), end_time=(timezone.now() + timezone.timedelta(hours=1)))
        a.save()
        w = Items.objects.create(name='Foo', description='Bar', price=1, auction=a)
        data = {'name': w.name, 'description': w.description, 'price': w.price, 'auction': w.auction}
        form = AddItemForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        a = Auction.objects.create(name='Foo', description='Bar',  start_time=timezone.now(), end_time=(timezone.now() + timezone.timedelta(hours=1)))
        a.save()
        w = Items.objects.create(name='Foo', description='', price=-1, auction=a)
        data = {'name': w.name, 'description': w.description, 'price': w.price, 'auction': w.auction}
        form = AddItemForm(data=data)
        self.assertFalse(form.is_valid())
