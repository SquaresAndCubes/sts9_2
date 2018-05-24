from django.urls import path
from . import views

urlpatterns = [

    path('test/', views.test, name='test'),

    #Home Landing Page
    path('', views.home, name='home'),
    #Setlists landing page most recent year
    path('setlists/', views.year, name='index'),
    #Setlists by year
    path('setlists/<int:year>/', views.year, name='year'),
    #Songs List Landing Page
    path('songs/', views.songs, name='songs'),
    #Specific Song Page
    path('songs/<str:song>', views.song, name='song'),
    #Stats Landing Page
    path('stats/', views.stats, name='stats'),

]