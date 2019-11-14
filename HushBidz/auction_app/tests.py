from django.test import TestCase
from .models import Auction
from django.utils import timezone
#from django.core.urlresolvers import reverse
from .forms import AddAuctionForm

# Create your tests here.

class AuctionTest(TestCase):

# test models
    def create_auction(self, name="test", description="test", auction_type=1, start_time=timezone.now(), end_time=(timezone.now() + timezone.timedelta(hours=1))):
        return Auction.objects.create(name=name, description=description, auction_type=auction_type, start_time=start_time, end_time=end_time)

    def test_whatever_creation(self):
        w = self.create_auction()
        self.assertTrue(isinstance(w, Auction))
        #self.assertEqual(w.__unicode__(), w.name)

#test forms
    def test_valid_form(self):
        w = Auction.objects.create(name='Foo', description='Bar', auction_type=1, start_time=timezone.now(), end_time=(timezone.now() + timezone.timedelta(hours=1)))
        data = {'name': w.name, 'description': w.description, 'auction_type': w.auction_type, 'start_time': w.start_time, 'end_time': w.end_time}
        form = AddAuctionForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = Auction.objects.create(name='Foo', description='', auction_type=0, start_time=timezone.now(), end_time=timezone.now())
        data = {'name': w.name, 'description': w.description, 'auction_type': w.auction_type, 'start_time': w.start_time, 'end_time': w.end_time}
        form = AddAuctionForm(data=data)
        self.assertFalse(form.is_valid())

#test views
#    def test_auction_list_view(self):
#        w = self.create_auction()
#        url = reverse("auction.views.auction")
#        resp = self.client.get(url)

#        self.assertEqual(resp.status_code, 200)
#        self.assertIn(w.name, resp.content)