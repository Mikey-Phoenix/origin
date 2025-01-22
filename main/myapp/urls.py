from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('home/', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('bids/', views.bids, name='bids'),
    path('make_bid/<art_id>', views.make_bid, name='make-a-bid'),
    path('about/', views.about, name='about')
]