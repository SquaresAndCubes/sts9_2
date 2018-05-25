from django.urls import path
from . import views

urlpatterns = [

    path('test/', views.test, name='test'),

    #Home Landing Page
    path('', views.home, name='home'),
    #Setlists landing page most recent year
    path('setlists/', views.setlists_by_year, name='setlist index'),
    #Setlists by year
    path('setlists/<int:year>/', views.setlists_by_year, name='setlists by year'),
    #Songs List Landing Page
    path('songs/', views.song_play_count, name='songs play count'),
    #Specific Song Page
    path('songs/<str:song_name>', views.song_details, name='song details'),
    #Stats Landing Page
    path('stats/', views.stats, name='stats'),

]