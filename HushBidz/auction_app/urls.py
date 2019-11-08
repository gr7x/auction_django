from django.urls import path
from django.conf.urls import url

from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/signup/$', views.signup, name='signup'),
    path('accounts/login/', authViews.LoginView.as_view(), name='login')
#    path('manage_auction', views.manage_auction, name='manage_auction'),
]
