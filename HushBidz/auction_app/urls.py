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
    path('add_items/<pk>/', views.add_items, name='add_items'),
    path('view_auction/<pk>/', views.view_auction, name='view_auction'),
    path('view_item/<pk>/<id>/', views.view_item, name='view_item'),
    path('user_page/', views.user_page, name='user_page'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('admin_auction_view/<pk>', views.admin_auction_view, name='admin_auction_view'),
    path('liveAuction/<pk>', views.liveAuction, name='liveAuction')
]
