from django.urls import path
from . import views

urlpatterns = [
    #About section
    path('test/', views.test, name='test'),

]