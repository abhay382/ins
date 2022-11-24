from django.urls import path

from . import views

urlpatterns = [
    

  path('', views.index, name='index'),
     path('gallery/', views.Gallery, name='index'),
     path('about/', views.about, name='index'),
     path('contact/', views.contact, name='index'),
     path('factoury/', views.fatory, name='index'),
     path('gallery/', views.Gallery, name='index'),
     path('seedpapers/', views.seed, name='index'),
     path('leatherjournal/', views.Leatherjournal, name='index'),
     path('christmas/', views.christ, name='index'),
     path('paperbags/', views.bag, name='index'),
     path('handmadepaper/', views.handmade, name='index'),
     path('lamp/', views.lamp, name='index'),
     path('boxes/', views.boxes, name='index'),
     path('gift/', views.gift, name='index'),
     path('cards/', views.cards, name='index'),
     path('query/', views.query, name='index'),


]
