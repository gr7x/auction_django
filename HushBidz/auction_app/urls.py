from django.urls import path
from django.conf.urls import url

from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/signup/$', views.signup, name='signup'),
    path('accounts/login/', authViews.LoginView.as_view(), name='login'),
    url(r'^create_auction$', views.create_auction, name='setup_auction'),
    url(r'^manage_auction$', views.manage_auction, name='manage_auction'),
    url(r'^add_items$', views.add_items, name='add_items'),
    url(r'^activate/'
      r'(?P<uidb64>[0-9A-Za-z_\-]+)/'
      r'(?P<token>[0-9A-Za-z]{1,13}'
      r'-[0-9A-Za-z]{1,20})/$',
      views.activate_account, name='activate'),
    url(r'^liveAuction$', views.liveAuction, name='liveAuction')
]
