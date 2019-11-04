from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^register/submit$', views.registerUser, name='registerUser'),
    url(r'^registrationConfirmation$', views.registrationConfirmation, name='registrationConfirmation'),
#    path('manage_auction', views.manage_auction, name='manage_auction'),
]
