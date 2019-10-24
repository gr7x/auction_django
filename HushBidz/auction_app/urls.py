from django.urls import path

from . import views

urlpatterns = [
    path('manage_auction', views.manage_auction, name='manage_auction'),
]