from django.urls import path
from django.conf.urls import url

from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/signup/$', views.signup, name='signup'),
    path('accounts/login/', authViews.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('create_auction', views.create_auction, name='setup_auction'),
    path('manage_auction', views.manage_auction, name='manage_auction'),
    path('add_items/<int:pk>/', views.add_items, name='add_items'),
    url(r'^liveAuction$', views.liveAuction, name='liveAuction')
]
