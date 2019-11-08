from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^create_auction$', views.create_auction, name='setup_auction'),
    url(r'^manage_auction$', views.manage_auction, name='manage_auction'),
    url(r'^add_items$', views.add_items, name='add_items'),
]
