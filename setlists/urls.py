from django.urls import path
from . import views

urlpatterns = [
    #About section
    path('test/', views.test, name='test'),
    path('', views.home, name='home'),
    path('setlists/<int:year>/', views.year, name='year'),
    path('songs/', views.songs, name='songs'),
    path('stats/', views.stats, name='stats'),

]