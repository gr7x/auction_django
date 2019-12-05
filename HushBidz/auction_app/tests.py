from django.test import TestCase
from .models import Auction, Items
from django.utils import timezone
from django.urls import reverse
from .forms import AddAuctionForm, AddItemForm
from django.core.exceptions import ValidationError


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
    def test_index(self):
        w = self.create_auction()
        url = reverse("index")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        #self.assertIn(w.name, resp.content)




class ItemTest(TestCase):

    def test_invalid_form(self):
        a = Auction.objects.create(name='Foo', description='Bar',  start_time=timezone.now(), end_time=(timezone.now() + timezone.timedelta(hours=1)))
        a.save()
        w = Items.objects.create(name='Foo', description='', price=-1, auction=a)
        data = {'name': w.name, 'description': w.description, 'price': w.price, 'auction': w.auction}
        form = AddItemForm(data=data)
        self.assertFalse(form.is_valid())

    def test_model_relation(self):
        x = Auction.objects.create(name="test1")
        y = Items(auction=Auction.objects.create(name="test2"))
        y.full_clean()  # `event` correctly set. This should pass
        y.save()
        self.assertEqual(Items.objects.filter(auction__name="test2").count(), 1)

    def test_model_relation__auction_missing(self):
        x = Auction.objects.create(name="test1")
        y = Items()  # Y without `event` set
        with self.assertRaises(ValidationError):
            y.full_clean()
            y.save()
        self.assertEqual(Items.objects.filter(auction__name="test2").count(), 0)
